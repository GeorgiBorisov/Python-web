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