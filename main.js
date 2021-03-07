
const DPR = window.devicePixelRatio;

function grid(ctx, origin, lineCount, squareWidth) {
  ctx.lineWidth = 1;
  ctx.strokeStyle = '#eee';

  const innerWidth = lineCount * squareWidth;

  ctx.beginPath();
  
  for (let i = 0; i < lineCount + 1; i++) {
    ctx.moveTo(origin.x + i * squareWidth * DPR, origin.y + 0);
    ctx.lineTo(origin.x + i * squareWidth * DPR, origin.y + innerWidth * DPR);
    ctx.stroke();
  }

  for (let i = 0; i < lineCount + 1; i++) {
    ctx.moveTo(origin.x + 0, origin.y + i * squareWidth * DPR);
    ctx.lineTo(origin.x + innerWidth * DPR, origin.y + i * squareWidth * DPR);
    ctx.stroke();
  }

  ctx.beginPath();
  ctx.strokeStyle = '#ccc';

  // bottom left to top right 1/2
  for (let i = 0; i < lineCount + 1; i++) {
    ctx.moveTo(origin.x,
               origin.y + (lineCount - i) * squareWidth * DPR);
    ctx.lineTo(origin.x + i * squareWidth * DPR,
               origin.y + innerWidth * DPR);
    ctx.stroke();
  }

  // bottom left to top right 2/2
  for (let i = 0; i < lineCount; i++) {
    ctx.moveTo(origin.x + i * squareWidth * DPR,
               origin.y + 0);
    ctx.lineTo(origin.x + innerWidth * DPR,
               origin.y + (lineCount - i) * squareWidth * DPR);
    ctx.stroke();
  }

  // top left to bottom right 1/2

  for (let i = 1; i < lineCount; i++) {
    ctx.moveTo(origin.x,
               origin.y + i * squareWidth * DPR);
    ctx.lineTo(origin.x + i * squareWidth * DPR,
               origin.y);
    ctx.stroke();
  }

  // top left to bottom right 2/2
  for (let i = 0; i < lineCount; i++) {
    ctx.moveTo(origin.x + i * squareWidth * DPR,
               origin.y + innerWidth * DPR);
    ctx.lineTo(origin.x + innerWidth * DPR,
               origin.y + i * squareWidth * DPR);
    ctx.stroke();
  }

  
}

function cutlines(ctx, origin, squareWidth) {

  ctx.beginPath();
  ctx.strokeStyle = 'black';

  // top
  ctx.moveTo(origin.x,
             origin.y);
  ctx.lineTo(origin.x + squareWidth * DPR * 16,
             origin.y);
  ctx.stroke();

  // bottom
  ctx.moveTo(origin.x,
             origin.y + squareWidth * 5/2 * DPR);
  ctx.lineTo(origin.x + squareWidth * DPR * 16,
             origin.y + squareWidth * 5/2 * DPR);
  ctx.stroke();

  for (var i = 0; i < 3; i++) {

    // primary down
    ctx.moveTo(origin.x + squareWidth * ((0 + i * 10) * DPR) / 2,
               origin.y + squareWidth * (0 * DPR) / 2);
    ctx.lineTo(origin.x + squareWidth * ((4 + i * 10) * DPR) / 2,
               origin.y + squareWidth * (4 * DPR) / 2);
    ctx.stroke();

    // primary up
    ctx.moveTo(origin.x + squareWidth * ((5 + i * 10) * DPR) / 2,
               origin.y + squareWidth * (5 * DPR) / 2);
    ctx.lineTo(origin.x + squareWidth * ((5 + 4 + i * 10) * DPR) / 2,
               origin.y + squareWidth * (1 * DPR) / 2);
    ctx.stroke();

    // secondary up
    ctx.moveTo(origin.x + squareWidth * ((4 + i * 10) * DPR) / 2,
               origin.y + squareWidth * (4 * DPR) / 2);
    ctx.lineTo(origin.x + squareWidth * ((5 + i * 10) * DPR) / 2,
               origin.y + squareWidth * (3 * DPR) / 2);
    ctx.stroke();

    // secondary down
    ctx.moveTo(origin.x + squareWidth * ((9 + i * 10) * DPR) / 2,
               origin.y + squareWidth * (1 * DPR) / 2);
    ctx.lineTo(origin.x + squareWidth * ((10 + i * 10) * DPR) / 2,
               origin.y + squareWidth * (2 * DPR) / 2);
    ctx.stroke();    
    
  }
  
}

document.addEventListener("DOMContentLoaded", function(event) {
  // Your code to run since DOM is loaded and ready
  const c = document.createElement("canvas");
  document.body.appendChild(c);
  const w = 600,
        h = 600;
  c.width = w * DPR;
  c.height = h * DPR;
  c.style['width'] = w + 'px';
  c.style['height'] = h + 'px';

  const ctx = c.getContext("2d");
  const origin = { x: 20 * DPR, y: 20 * DPR };

  const lineCount = 16;
  const squareWidth = 30;

  grid(ctx, origin, lineCount, squareWidth);
  cutlines(ctx, origin, squareWidth);
  
});
