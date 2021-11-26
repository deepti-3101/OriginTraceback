
window.addEventListener('DOMContentLoaded', () => 
{
const button = "<button style = 'position: absolute; z-index:100; background:blue; color:white; width:200px; height: 100px;' onclick= 'window.alert(\"Button Clicked\")'>test</button> "
document.body.innerHTML += button;
})
