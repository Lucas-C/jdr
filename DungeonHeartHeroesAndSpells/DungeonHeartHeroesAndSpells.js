// On remplace les cellules du tableau par le contenu des divs correspondants
let tbody = document.querySelector('.choices tbody')
document.querySelectorAll('div').forEach(div => {
    let className = div.classList[0]
    if (!className || !className.startsWith('td')) return
    let tdIndex = +className.charAt(2)
    let row = tdIndex < 3 ? tbody.children[0] : tbody.children[2]
    row.children[tdIndex % 3].innerHTML = div.innerHTML
    div.parentNode.removeChild(div)
})