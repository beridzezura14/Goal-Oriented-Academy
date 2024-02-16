const filterImg = document.querySelectorAll('.images img')
const filterabletext = document.querySelectorAll('.heroText')
const bgImage = document.querySelectorAll('.bg-image')

console.log(filterImg)


const filter = e => {
    document.querySelector('.active').classList.remove('active');
    e.target.classList.add('active')
    // console.log(e.target)

    // add hide class
    filterabletext.forEach(card => {
        card.classList.add('hide')
        if(card.dataset.name === e.target.dataset.name){
            card.classList.remove('hide')
        }
    })
    bgImage.forEach(img => {
        img.classList.add('hide')
        if(img.dataset.name === e.target.dataset.name){
            img.classList.remove('hide')
        }
    })
}
filterImg.forEach(button => button.addEventListener('click', filter))
