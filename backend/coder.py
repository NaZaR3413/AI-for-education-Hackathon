import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from hnsqlite import Collection
import numpy as np
from numpy import dot
from numpy.linalg import norm
import tiktoken
from download import parsed_data

load_dotenv()

#key = os.getenv("API_KEYH")

skills_collection = Collection(collection_name="skills",dimension=1536)
text_collection = Collection(collection_name="text", dimension=1536)
exp_collection = Collection(collection_name="experience", dimension=1536)
client = OpenAI(api_key="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")

with open("./hrflow-profiles (1).json","r", encoding="utf8") as j:
    data = json.loads(j.read())

data[0].keys()

exp_embeddings = {'text':[],'id':[],'vector':[]}
skills_embeddings = {'text':[],'id':[],'vector':[]}
text_embeddings = {'text':[],'id':[],'vector':[]}

for i in range(len(data)):
    for j in range(len(data[i]['experiences'])):
        exp_embeddings['text'].append(data[i]['experiences'][j]['description'])
        exp_embeddings['id'].append(i)
    skills_embeddings['text'].append(', '.join([j['name'] for j in data[i]['skills']]))
    skills_embeddings['id'].append(i)
    text_embeddings['text'].append(data[i]['text'])
    text_embeddings['id'].append(i)

exp_embed = client.embeddings.create(input=exp_embeddings['text'], model="text-embedding-3-small")
skills_embed = client.embeddings.create(input=skills_embeddings['text'], model="text-embedding-3-small")
text_embed = client.embeddings.create(input=text_embeddings['text'], model="text-embedding-3-small")

exp_embeddings['vector'] = []
skills_embeddings['vector'] = []
text_embeddings['vector'] = []
for i in range(len(exp_embed.data)):
    exp_embeddings['vector'].append(np.array(exp_embed.data[i].embedding))

for i in range(len(skills_embed.data)):
    skills_embeddings['vector'].append(np.array(skills_embed.data[i].embedding))

for i in range(len(text_embed.data)):
    text_embeddings['vector'].append(np.array(text_embed.data[i].embedding))

exp_collection.add_items(exp_embeddings['vector'], exp_embeddings['text'], exp_embeddings['id'])
skills_collection.add_items(skills_embeddings['vector'], skills_embeddings['text'], skills_embeddings['id'])
text_collection.add_items(text_embeddings['vector'], text_embeddings['text'], text_embeddings['id'])

text_collection.count(), skills_collection.count(), exp_collection.count()

resume = data[0]
exps = [resume['experiences'][i]['description'] for i in range(len(resume['experiences']))]
skills = [', '.join([i['name'] for i in resume['skills']])]
text = [resume['text']]

embeddings = client.embeddings.create(input=exps+skills+text, model="text-embedding-3-small")

embeddings = [np.array(embed.embedding) for embed in embeddings.data]
text_collection.search(embeddings[-1], k=5)

def query():
    with open("jd.txt", "r") as f:
        jd = f.read()
    prompt = """extract skills required, summary on about the company, and job responsibilities for the following
    job description in form of python dictionary with "skills_required", "summary", "job_responsibilities" words as respective keywords. return only dictionary and nothing else.

    {jd}""".format(jd=jd)

    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system", "content":"you are a resume reviewer helping students get their desired job"},
                {"role":"user", "content":prompt}]
    )

    print(res.choices[0].message.content)

    et = "d="+res.choices[0].message.content

    exec(et, globals())

    jde = client.embeddings.create(input=[jd, ', '.join(d["skills_required"]), d["summary"], '\n'.join(d["job_responsibilities"])], model="text-embedding-3-small")
    jde = [np.array(i.embedding) for i in jde.data]

    text_ids = [i.doc_id for i in text_collection.search(jde[0], k=5)]
    skills_ids = [i.doc_id for i in skills_collection.search(jde[1], k=5)]
    exp_ids = [i.doc_id for i in exp_collection.search(jde[3], k=5)]

    sd = {}
    for i in range(len(text_ids)):
        if text_ids[i] not in sd.keys():
            sd[text_ids[i]] = 5-i
        else:
            sd[text_ids[i]] = sd[text_ids[i]] + (5-i)
        if skills_ids[i] not in sd.keys():
            sd[skills_ids[i]] = 5-i
        else:
            sd[skills_ids[i]] = sd[skills_ids[i]] + (5-i)
        if exp_ids[i] not in sd.keys():
            sd[exp_ids[i]] = 5-i
        else:
            sd[exp_ids[i]] = sd[exp_ids[i]] + (5-i)
    

    r = int(list({k:v for k,v in sorted(sd.items(), key=lambda i:i[1], reverse=True)}.keys())[0])
    print(r)

    #with open("./test_resume.json","r", encoding="utf8") as j:
     #   test_data = json.loads(j.read())
    test_data = parsed_data

    candidate_resume = test_data
    success_resume = data[r]["text"]

    prompt = """extract action keywords and impact keywords from the following two resume and job description seperately.
    Return the result as a dictionary with resume1_action_keywords, resume2_action_keywords, jd_action_keywords,
    resume1_impact_keywords, resume2_impact_keywords, jd_impact_keywords as keys and the results as values. return only dictionary and nothing else.

    Resume1
    {candidate_resume}

    Resume2
    {success_resume}

    job description
    {jd}

    """.format(candidate_resume = candidate_resume, success_resume = success_resume, jd = jd)
    k = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"system", "content":"you are a resume reviewer helping students get their desired job"},
                {"role":"user", "content":prompt}]
                )
    
    k_choice = k.choices[0].message.content
    #hr = k_choice.sprie
    k_choice = k_choice.strip("python")
    et = "resd="+k_choice
    
    exec(et, globals())

    sskills = [i["name"].lower() for i in data[r]["skills"]]
    cskills = [i["name"].lower() for i in test_data["skills"]]
    jd_skills = [i.lower() for i in d["skills_required"]]
    sact = [i.lower() for i in resd["resume2_action_keywords"]]
    cact = [i.lower() for i in resd["resume1_action_keywords"]]
    jact = [i.lower() for i in resd["jd_action_keywords"]]
    simpact = [i.lower() for i in resd["resume2_impact_keywords"]]
    cimpact = [i.lower() for i in resd["resume1_impact_keywords"]]
    jdimpact = [i.lower() for i in resd["jd_impact_keywords"]]

    skill_score = 0
    for i in cskills:
        if i in sskills and i in jd_skills:
            skill_score = skill_score + 3
        elif i in sskills and i not in jd_skills:
            skill_score = skill_score + 1
        elif i not in sskills and i in jd_skills:
            skill_score = skill_score + 5
    
    
    ai_embeddings = client.embeddings.create(input = [', '.join(cact),
                                                  ', '.join(jact),
                                                  ', '.join(cimpact),
                                                  ', '.join(jdimpact)], model = "text-embedding-3-small")
    
    
    ai_embeddings = [np.array(i.embedding) for i in ai_embeddings.data]

    cembeddings = []
    cembed = client.embeddings.create(input=[i["description"] for i in test_data["experiences"]], model="text-embedding-3-small")
    cembeddings = [np.array(i.embedding) for i in cembed.data]

    def cosine(a,b):
        return dot(a, b)/(norm(a)*norm(b))
    jr_score = 0
    js_score = 0
    for i in cembeddings:
        jr_score = jr_score + cosine(i, jde[3])
        js_score = js_score + cosine(i, jde[2])
    jr_score = jr_score/len(cembeddings)
    js_score = js_score/len(cembeddings)

    jr_score = ((jr_score+1)/2)*100
    js_score = ((js_score+1)/2)*100
    action_score = (cosine(ai_embeddings[0], ai_embeddings[1])+1)*50
    impact_score = (cosine(ai_embeddings[2], ai_embeddings[3])+1)*50
    scores_calc = [skill_score, action_score, impact_score, jr_score, js_score]
    return [skill_score, action_score, impact_score, jr_score, js_score]


print(query())
