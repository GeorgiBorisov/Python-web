document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.profile-delete').addEventListener('click', () => {
        document.querySelector('.bg-modal').style.display='flex'
    })
})

document.querySelector('.close').addEventListener('click', () => {
    document.querySelector('.bg-modal').style.display='none'
})

document.querySelector('.cancel-delete').addEventListener('click', () => {
    document.querySelector('.bg-modal').style.display='none'
})