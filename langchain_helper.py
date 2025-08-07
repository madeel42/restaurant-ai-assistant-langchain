from secret_key import gemni_key
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os
os.environ["GOOGLE_API_KEY"] = gemni_key

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

def generate_restaurant_name_and_items(cuisine):
    promptsTemplate_name = PromptTemplate(input_variables=["cuisine"],
                                          template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.just one name")
    name_chain = LLMChain(llm=llm, prompt=promptsTemplate_name, output_key="restaurant_name")

    promptsTemplate_name = PromptTemplate(input_variables=["restaurant_name"],
                                          template="Suggest some menu item for {restaurant_name} food. separated by come , just give 3 to 4 item")
    food_item_chain = LLMChain(llm=llm, prompt=promptsTemplate_name, output_key="menu_item")
    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_item"]
    )

    result = chain.invoke({"cuisine": cuisine})
    return result

if __name__ == '__main__':
    result = generate_restaurant_name_and_items("indian")
    print(result)