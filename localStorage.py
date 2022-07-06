import streamlit as st

st.components.v1.html("""
<input type="text" id="myText">
<button id="setButton">set it</button>
<button id="getButton">get it</button>
<button id="setC">set cookie</button>
<button id="getC">get cookie</button>
<script>
    const set = () => {
        const txt = document.getElementById('myText').value
        window.localStorage.setItem('bob', txt)
    }
    
    const get = () => {
        alert(localStorage.getItem('bob'))
    }
    
    const setC = () => {
        const txt = document.getElementById('myText').value
        document.cookie = `bob=${txt}; sameSite=none; secure=true; path=/`
    }
    
    const getC = () => {
        alert(document.cookie)
    }
    
    
    document.getElementById('setButton').addEventListener('click', set)
    document.getElementById('getButton').addEventListener('click', get)
    document.getElementById('setC').addEventListener('click', setC)
    document.getElementById('getC').addEventListener('click', getC)
</script>
""")
