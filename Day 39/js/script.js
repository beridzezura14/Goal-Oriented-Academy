const navDiv = document.querySelector('.nav-div');

window.addEventListener('scroll', function(){
    navDiv.classList.toggle('sticky', window.scrollY > 0);
})

// start responsive menu 
const open = document.querySelector('.open');
const close = document.querySelector('.close')
const navbar = document.querySelector('.navbar ul')

open.addEventListener('click', function(){
    navbar.style.display = 'flex'
    open.style.display = 'none'
    close.style.display = 'block'
})

close.addEventListener('click', function(){
    navbar.style.display = 'none'
    open.style.display = 'block'
    close.style.display = 'none'
})

// start project section
const filterButton = document.querySelectorAll('.items li')
const filterableItems = document.querySelectorAll('.all-projects')
const active = document.querySelector('.active')
const filterCards = e => { 
    document.querySelector('.active').classList.remove('active');
    e.target.classList.add('active')
    console.log(e.target)

    // add hide class
    filterableItems.forEach(card => {
        card.classList.add('hide')
        if(card.dataset.name === e.target.dataset.name){
            card.classList.remove('hide')
        }
    })
}
for(i = 0; i < filterButton.length; i++){
    filterButton[i].addEventListener('click', filterCards)
}

// filterCards()
// filterButton.forEach(button => button.addEventListener('click', filterCards))
// filterButton.addEventListener('click', filterCards)
