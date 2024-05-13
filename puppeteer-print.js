const path = require('path');
const puppeteer = require('puppeteer')

(async () => {
    const url = `file://${path.resolve(process.argv[2])}`
    const outFilePath = process.argv[3]
    console.log(`${url} -> ${outFilePath}`)
    const browser = await puppeteer.launch({ headless: true })
    try {
        const page = await browser.newPage()
        await page.goto(url, { waitUntil: 'networkidle2' })
        await page.pdf({
            path: outFilePath,
            height: 1055,
            width: 815,
            outline: true,
        })
    } finally {
        await browser.close()
    }
})()
