import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain, SequentialChain
import uuid
import streamlit.components.v1 as components
import html

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

## Setting ChatGroq with parameters for llm setup
groqAiLLM = ChatGroq(
    api_key=GROQ_API_KEY,
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
) 

# Title with Streamlit
st.title("Product Description Generator")

# Custom copy button function
def create_copy_button(text_to_copy):
    button_id = f"copyButton-{uuid.uuid4().hex}"
    escaped_text = html.escape(text_to_copy).replace('"', '&quot;')

    button_html = f"""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <button id="{button_id}" style="padding: 6px 10px; background-color: #4CAF50; color: white;
                                     display: inline-flex; align-items: center; justify-content: center;
                                     border-radius: 25px; font-size: 16px; border: none; cursor: pointer;">
        <i class="fa fa-copy"></i>
    </button>
    <script>
        let copyButton = document.getElementById("{button_id}")
        if(copyButton){{
            copyButton.addEventListener('click', function(){{
                navigator.clipboard.writeText("{escaped_text}").then(() => {{
                    alert("Copied to clipboard!")
                }}).catch(() => {{
                    alert("Failed to copy")
                }})
            }})
        }}
    </script>
    """
    components.html(button_html, height=100)


# Sequential Chain Setup
def create_sequential_chain():
    # Template for Product Title Generation
    title_template = '''
You are a seasoned SEO specialist with deep expertise in digital sales and marketing copywriting.

Your task is to craft a compelling, creative, and attention-grabbing product title that:
- Begins with one or two bold, exclusive, and premium-sounding words that convey a sense of quality and effectiveness to the end user.
- Clearly highlights the product's key feature.
- Appeals to the target audience's emotions, needs, or desires.
- Incorporates relevant keywords for optimal SEO visibility.
- Is concise (preferably under 70 characters), yet impactful and engaging.

Use the information below:
- Product Name: {product_name}
- Key Feature: {product_feature}

Respond with only the final product title as plain text—no formatting, explanations, or additional output.
'''

    # Template for Product Description Generation
    description_template = '''
You are a seasoned marketing copywriter with expertise in persuasive product descriptions and conversion-focused content.

Your task is to write a compelling, engaging, and benefit-driven product description based on the following product title:
- Product Title: {product_title}

The description should:
- Expand on the product's key benefits and what makes it stand out.
- Emphasize its value, efficiency, and appeal to the target customer's desires or problems.
- Maintain a confident, persuasive marketing tone.
- Be concise, ideally between 50 to 100 words.
- Be suitable for use on an e-commerce website or digital marketplace.

Respond with only the final product description as plain text—no formatting, explanations, or additional output.
'''

    # Template for Caption Generation
    caption_template = '''
You are a professional social media copywriter skilled in crafting engaging, concise, and brand-aligned captions for various digital platforms.

Your task is to write a high-quality social media caption based on the following product information:

- Product Title: {product_title}
- Product Description: {product_description}

Incorporate the following elements:
- SEO Keyword: {seo_keyword} (e.g., a key term that enhances search visibility)
- Tone/Style: {tone} (e.g., bold, luxurious, elegant, modern, minimalist, warm, fun, modern, inspiring)

The caption must:
- Grab attention in the first line.
- Highlight a key benefit, use case, or emotional appeal.
- Seamlessly include the SEO keyword.
- End with a light call-to-action (e.g., try it, learn more, tap to explore).
- Fit within 30–70 words for ideal platform performance.

Platform: {platform} (e.g., Instagram, LinkedIn, Facebook, Twitter, YouTube, Email)

Respond with only the final caption—no formatting, hashtags, or additional commentary.
'''

    # Create Prompt Templates
    title_prompt = PromptTemplate(
        input_variables=["product_name", "product_feature"],
        template=title_template
    )
    
    description_prompt = PromptTemplate(
        input_variables=["product_title"],
        template=description_template
    )
    
    caption_prompt = PromptTemplate(
        input_variables=["product_title", "product_description", "seo_keyword", "tone", "platform"],
        template=caption_template
    )

    # Create Individual LLM Chains
    title_chain = LLMChain(
        llm=groqAiLLM,
        prompt=title_prompt,
        output_key="product_title"
    )
    
    description_chain = LLMChain(
        llm=groqAiLLM,
        prompt=description_prompt,
        output_key="product_description"
    )
    
    caption_chain = LLMChain(
        llm=groqAiLLM,
        prompt=caption_prompt,
        output_key="caption"
    )

    # Create Sequential Chain
    sequential_chain = SequentialChain(
        chains=[title_chain, description_chain, caption_chain],
        input_variables=["product_name", "product_feature", "seo_keyword", "tone", "platform"],
        output_variables=["product_title", "product_description", "caption"],
        verbose=True
    )
    
    return sequential_chain

## Function for Streamlit output using Sequential Chain
def streamlit_output(product_name, product_feature, seo_keyword, tone, platform):
    try:
        # Create and run the sequential chain
        chain = create_sequential_chain()
        
        # Execute the chain with all inputs
        result = chain({
            "product_name": product_name,
            "product_feature": product_feature,
            "seo_keyword": seo_keyword,
            "tone": tone,
            "platform": platform
        })
        
        # Display results in columns
        if result:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.write("**Product Title:**")
                colA, colB = st.columns([3, 1])
                with colA:
                    st.write(result["product_title"])
                with colB:
                    create_copy_button(result["product_title"])
            
            with col2:
                st.write("**Product Description:**")
                colA, colB = st.columns([3, 1])
                with colA:
                    st.markdown(
                        f"""
                        <div style="
                            border: 1px solid #ccc;
                            padding: 10px;
                            height: 300px;
                            overflow-y: auto;
                            background-color: #171515;
                            white-space: pre-wrap;
                            font-family: Arial, sans-serif;
                            border-radius: 5px;
                        ">
                            {result["product_description"].strip()}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                with colB:
                    create_copy_button(result["product_description"])
            
            with col3:
                st.write("**Caption:**")
                colA, colB = st.columns([3, 1])
                with colA:
                    st.write(result["caption"])
                with colB:
                    create_copy_button(result["caption"])
                    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

## Form using Streamlit
with st.container():
    with st.form("product_form"):
        st.markdown("### Enter Product Information")
        
        ProductName = st.text_input(
            "Product Name:",
            placeholder="e.g., Smart Contact lenses"
        )
        
        ProductFeature = st.text_area(
            "Product Feature:",
            placeholder="e.g., Track your health with our innovative smart contact lenses that monitor vital signs and provide real-time data."
        )
        
        SEOKeyword = st.text_input(
            "SEO Keyword:",
            placeholder="e.g., smart contact lenses, health monitoring lenses, innovative eyewear, temperature adaptor"
        )
        
        Tone = st.text_input(
            "Tone/Style:",
            placeholder="e.g., elegant, modern, warm, fun, inspiring, bold, luxurious, minimalist"
        )
        
        Platform = st.selectbox(
            "Select Platform:", 
            ["Instagram", "LinkedIn", "Facebook", "Twitter", "YouTube", "Email"]
        )
        
        submitted = st.form_submit_button("Generate Content", type="primary")
        
        if submitted:
            if not all([ProductName, ProductFeature, SEOKeyword, Tone, Platform]):
                st.warning("Please fill in all fields to generate content.")
            else:
                with st.spinner("Generating content..."):
                    streamlit_output(
                        product_name=ProductName,
                        product_feature=ProductFeature, 
                        seo_keyword=SEOKeyword,
                        tone=Tone,
                        platform=Platform
                    )

## Footer
st.markdown("---")
st.markdown("*©2025 Tanya Kumari*")
