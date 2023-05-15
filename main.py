import streamlit as st
import os
import uuid
from functions import *
import plantuml

st.title("User Story to use case diagram")

text = st.text_area("Enter your text", height=200)
btn = st.button("Generate")

if btn:
    text = preprocess_text(text)
    classes_attr = get_classes_attributes(text)
    inheritances = get_inheritance(text, classes_attr.keys())
    relations = get_relationships(text, classes_attr.keys(), inheritances)
    graph = graph_from_uml(classes_attr, relations, inheritances)
    ###############################################################
    uml=classes_attr
    actors=[]
    actor_relations=[]
    for cls in uml.keys():
        attributes=list(uml[cls])
        if attributes:
            actors=[]
            actors.append(cls)
            actors.append(attributes)
            actor_relations.append(actors)
    uml_code = "@startuml\n\n"
    for actor, relations in actor_relations:
        uml_code += f"actor {actor}\n"
        for relation in relations:
            uml_code += f"{actor} --> ({relation})\n"
    uml_code += "\n@enduml"
    plantuml_url = "http://www.plantuml.com/plantuml/img/"
    image = plantuml.PlantUML(url=plantuml_url).processes(uml_code)
    with open("use_12.png", "wb") as f:
        f.write(image)
    #image_url = str(uuid.uuid1()) + ".png"
    #print(image_url)
    #image.write_png(image_url)
    st.image("use_12.png")
    #os.remove(image_url)