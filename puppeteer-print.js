// USAGE: node puppeteer-print.js $htmlFile $outPdfFile [$pageFormat as ${width}x${height}] [${horizMargin}x${vertiMargin}]

const path = require('path');
const puppeteer = require('puppeteer');

(async () => {
    const url = `file://${path.resolve(process.argv[2])}`
    const outFilePath = process.argv[3]
    let pageFormat = process.argv[4]
    const outerMargin = process.argv[5]
    let height, width
    if (pageFormat) {
        [width, height] = pageFormat.split('x')
        width = Number.parseInt(width, 10)
        height = Number.parseInt(height, 10)
    } else {
        // Default format:
        pageFormat = "US letter"
        height = 1055
        width = 815
    }
    let horizMargin, vertiMargin
    if (outerMargin) {
        [horizMargin, vertiMargin] = outerMargin.split('x')
        horizMargin = Number.parseInt(horizMargin, 10)
        vertiMargin = Number.parseInt(vertiMargin, 10)
    } else {
        // Default margin:
        horizMargin = 25
        vertiMargin = 25
        // This should be overridable in CSS by: @media print { @page { margin: ... } }
        // though on 2026/04/20 I could not make it work with 2200_le_jugement_des_dieux...
    }
    console.log(`${url} -> ${outFilePath} (format: ${pageFormat} / margin: ${horizMargin}x${vertiMargin})`)
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
            height,
            width,
            margin: {
                bottom: vertiMargin,
                top: vertiMargin,
                left: horizMargin,
                right: horizMargin,
            },
            outline: true,
        })
    } finally {
        await browser.close()
    }
})()
