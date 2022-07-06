import streamlit as st

st.components.v1.html("""
<input type="text" id="myText">
<button id="setButton">set it</button>
<button id="getButton">get it</button>
<script>
    const set = () => {
        const txt = document.getElementById('myText').value
        window.localStorage.setItem('bob', txt)
    }
    
    const get = () => {
        alert(localStorage.getItem('bob'))
    }
    
    
    document.getElementById('setButton').addEventListener('click', set)
    document.getElementById('getButton').addEventListener('click', get)
</script>
""")
