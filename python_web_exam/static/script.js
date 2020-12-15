if(document.querySelector('.bg-modal')){
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelector('.profile-delete, .post-delete').addEventListener('click', () => {
            document.querySelector('.bg-modal').style.display='flex'
        })
    })
    
    document.querySelector('.close').addEventListener('click', () => {
        document.querySelector('.bg-modal').style.display='none'
    })
    
    document.querySelector('.cancel-delete').addEventListener('click', () => {
        document.querySelector('.bg-modal').style.display='none'
    })
}

document.querySelector('.mobile-menu').addEventListener('click', () => {
    document.querySelector('.bar-two').classList.toggle('rotated')
    document.querySelector('.bar-one').classList.toggle('rotated')
    document.querySelector('.bar-three').classList.toggle('rotated')
    document.querySelector('.menu-wrapper').classList.toggle('show')
})

// const nav = document.querySelector('.menu-container')
// const navTop = nav.offsetTop
// debounce = (func, wait) => {
// 	let timeout
// 	return function() {
//         let context = this, 
//             args = arguments
// 		let later = function() {
// 			timeout = null
// 		}
// 		let callNow = !timeout
// 		clearTimeout(timeout)
// 		timeout = setTimeout(later, wait)
// 		if (callNow) {
//             func.apply(context, args)
//         } 
// 	}
// }
// fixedNav = debounce( () => {
//     console.log(window.scrollY)
//     console.log(nav.offsetTop)
//     if (window.scrollY >= navTop){
//         nav.classList.add('fixed')
//         document.querySelector('main').classList.add('fixed-active')
//     } else {
//         nav.classList.remove('fixed')
//         document.querySelector('main').classList.remove('fixed-active')
//     }
// }, 25)

// window.addEventListener('scroll', fixedNav)