// Source: https://www.beyondjava.net/blog/how-to-connect-html-elements-with-an-arrow-using-svg/

function connect(args) {
    const leftPos = args.left.getBoundingClientRect();
    args.x1 = leftPos.right;
    args.x1 += (args.leftXOffset || 0);
    args.y1 = leftPos.y;
    args.y1 += (args.left.offsetHeight / 2) + (args.leftYOffset || 0);
    
    const rightPos = args.right.getBoundingClientRect();
    args.x2 = rightPos.left;
    args.x2 += (args.rightXOffset || 0);
    args.y2 = rightPos.y;
    args.y2 += (args.right.offsetHeight / 2) + (args.rightYOffset || 0);

    const radius = args.circleRadius || 5;
    if (args.leftCircle) drawCircle({x:args.x1, y:args.y1, radius:radius, color:args.color});
    if (args.rightCircle) drawCircle({x:args.x2, y:args.y2, radius:radius, color:args.color});
    drawCurvedLine(args);
}

function drawCircle(args) {
    const svg = createSVG();
    const shape = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    shape.setAttributeNS(null, 'cx', args.x);
    shape.setAttributeNS(null, 'cy', args.y);
    shape.setAttributeNS(null, 'r',  args.radius);
    shape.setAttributeNS(null, 'fill', args.color);
    svg.appendChild(shape);
}

function drawCurvedLine(args) {
    const svg = createSVG();
    const shape = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    const delta = (args.x2 - args.x1) * (args.tension || 1);
    const hx1 = args.x1 + delta;
    const hy1 = args.y1;
    const hx2 = args.x2 - delta;
    const hy2 = args.y2;
    const path = 'M '  + args.x1 + ' ' + args.y1 +
               ' C ' + hx1 + ' ' + hy1
                     + ' '  + hx2 + ' ' + hy2
               + ' ' + args.x2 + ' ' + args.y2;
    shape.setAttributeNS(null, 'd', path);
    shape.setAttributeNS(null, 'fill', 'none');
    shape.setAttributeNS(null, 'stroke', (args.color || 'black'));
    shape.setAttributeNS(null, 'stroke-width', args.strokeWidth || 3);
    svg.appendChild(shape);
}

function createSVG() {
    let svg = document.getElementById('svg-canvas');
    if (null == svg) {
        svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('id', 'svg-canvas');
        svg.setAttribute('style', 'position:absolute; top:0px; left:0px');
        svg.setAttribute('width', document.body.clientWidth);
        svg.setAttribute('height', document.body.clientHeight);
        svg.setAttributeNS('http://www.w3.org/2000/xmlns/',
                           'xmlns:xlink',
                           'http://www.w3.org/1999/xlink');
        document.body.appendChild(svg);
    }
    return svg;
}

function removeSVG() {
    const svg = document.getElementById('svg-canvas');
    if (null != svg) {
        svg.parentNode.removeChild(svg);
    }
}
