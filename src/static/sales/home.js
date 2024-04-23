console.log("Hello World!")

const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')

console.log(reportBtn)
console.log(img)

if (img) {
    reportBtn.classList.remove('not-visible')
}