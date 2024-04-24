console.log("Hello World!")

const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')
const modalBody = document.getElementById('modal-body')
const reportForm = document.getElementById('report-form')

const reportName = document.getElementById('id_name')
const reportRemarks = document.getElementById('id_remarks')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

console.log(reportName)
console.log(reportRemarks)
console.log(csrf)

console.log(reportBtn)
console.log(img)

if (img) {
    reportBtn.classList.remove('not-visible')
}

reportBtn.addEventListener('click', ()=>{
    console.log('clicked')
    img.setAttribute('class', 'w-100')
    modalBody.prepend(img)

    console.log(img.src)

    reportForm.addEventListener('submit', e=>{
        e.preventDefault()
        const formData = new FormData()
        formData.append('csrfmiddlewaretoken', csrf)
        formData.append('name', reportName)
        formData.append('remarks', reportRemarks)
        formData.append('image', img.src)

        $.ajax({
            type: 'POST',
            url: 'reports/save/',
            data: formData,
            success: function(response){
                console.log(response)
            },
            error: function(error){
                console.log(error)
            },
            processData: false,
            contentType: false,
        })
    })
})