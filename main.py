import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="랭체인 튜토리얼",
    page_icon="👋",
)

st.write("# cbw https 적용 LangChain Tutorial!👋") 

st.sidebar.success("아래에 있는 데모 선택")
st.sidebar.markdown(""" - [LangChain Introduction](https://python.langchain.com/docs/get_started/introduction) """)
st.sidebar.markdown(""" - [LangChain Installation](https://python.langchain.com/docs/get_started/installation) """)
st.sidebar.markdown(""" - [LangChain Security](https://python.langchain.com/docs/security) """)
st.sidebar.markdown(""" - [Streamlit iframe API](https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.iframe) """)

st.write('For bigger screen, click the link below.')
st.markdown(""" - [LangChain Doc](https://python.langchain.com/v0.1/docs/get_started/introduction/) """)

# embed streamlit docs in a streamlit app
components.iframe("https://python.langchain.com/v0.1/docs/get_started/introduction/", height =1000, width = 1400, scrolling=True)

st.write('')
st.write('# CatchUp AI related materials')
st.write('')

st.markdown(
    """
    - [Catchup AI Streamlit Web App](https://catchupai.streamlit.app/)
    - [Catchup AI for Small Business App](https://catchupai4sb.streamlit.app/)
    - [Catchup AI Youtube Channel](https://www.youtube.com/@catchupai)
    - [Catchup AI Tistory Blog](https://coronasdk.tistory.com/)
    - [Deep Learning Fundamental PPT (Eng. Ver.)](https://docs.google.com/presentation/d/1F4qxSAv9g13de99rS8fcp4e1LCfrILq8QaahXCPx1Pw/edit?usp=sharing)
    - [Deep Learning Fundamental PPT (Kor. Ver.)](https://docs.google.com/presentation/d/15KNzGnSnJx_4ToSBM2MrHiC2q5MiVe0plOs7f3NJuWM/edit?usp=sharing)
    - [AI Web App Development 101 PPT](https://docs.google.com/presentation/d/18_6z05tmR_loTPWFHj8PCY3-uCNKuoy-IvE0g5ms8YM/edit?usp=sharing)
"""
)
