const path = require('path');
const puppeteer = require('puppeteer');

// This can be overriden in CSS by: @media print { @page { margin: ... } }
const DEFAULT_MARGIN = 25;

(async () => {
    const url = `file://${path.resolve(process.argv[2])}`
    const outFilePath = process.argv[3]
    console.log(`${url} -> ${outFilePath}`)
    const browser = await puppeteer.launch({
        // Unsafe but else fails in Github Actions pipeline:
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
        headless: true
    })
    try {
        const page = await browser.newPage()
        await page.goto(url, { waitUntil: 'networkidle2' })
        await page.pdf({
            path: outFilePath,
            // Default format: US letter
            height: 1055,
            width: 815,
            margin: {
                bottom: DEFAULT_MARGIN,
                top: DEFAULT_MARGIN,
                left: DEFAULT_MARGIN,
                right: DEFAULT_MARGIN,
            },
            outline: true,
        })
    } finally {
        await browser.close()
    }
})()
