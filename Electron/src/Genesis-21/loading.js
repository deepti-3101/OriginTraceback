//CANVAS
(function () {
    var canvas = document.querySelector("canvas"),
      ctx = canvas.getContext("2d");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    ctx.lineWidth = 0.3;
    ctx.strokeStyle = new Color(150).style;
  
    var mousePosition = {
      x: (30 * canvas.width) / 100,
      y: (30 * canvas.height) / 100,
      vx: 1.5,
      vy: 1.5
    };
  
    var dots = {
      nb: (canvas.width / 5).toFixed(1),
      nbMax: (canvas.width / 5).toFixed(1),
      distance: (canvas.width / 8).toFixed(1),
      d_radius: 150,
      array: []
    };
  
    function colorValue(min) {
      return Math.floor(Math.random() * 255 + min);
    }
  
    function createColorStyle(r, g, b) {
      return "rgba(" + r + "," + g + "," + b + ", 0.8)";
    }
  
    function mixComponents(comp1, weight1, comp2, weight2) {
      return (comp1 * weight1 + comp2 * weight2) / (weight1 + weight2);
    }
  
    function averageColorStyles(dot1, dot2) {
      var color1 = dot1.color,
        color2 = dot2.color;
  
      var r = mixComponents(color1.r, dot1.radius, color2.r, dot2.radius),
        g = mixComponents(color1.g, dot1.radius, color2.g, dot2.radius),
        b = mixComponents(color1.b, dot1.radius, color2.b, dot2.radius);
      return createColorStyle(Math.floor(r), Math.floor(g), Math.floor(b));
    }
  
    function Color(min) {
      min = min || 0;
      this.r = colorValue(min);
      this.g = colorValue(min);
      this.b = colorValue(min);
      this.style = createColorStyle(this.r, this.g, this.b);
      this.dimmerStyle = createColorStyle(this.r - 20, this.g - 20, this.b - 20);
      this.brighterStyle = createColorStyle(
        this.r + 20,
        this.g + 20,
        this.b + 20
      );
    }
  
    function Dot() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
  
      this.vx = -1.5 + Math.random();
      this.vy = -0.5 + Math.random();
  
      this.radius = Math.random() * 3;
  
      this.color = new Color();
      //console.log(this);
    }
  
    Dot.prototype = {
      draw: function () {
        ctx.beginPath();
        ctx.fillStyle = this.color.dimmerStyle;
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.fill();
      },
  
      drawBold: function () {
        ctx.beginPath();
        ctx.fillStyle = this.color.style;
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.fill();
  
        ctx.strokeStyle = this.color.brighterStyle;
        //ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
        ctx.arc(this.x, this.y, this.radius + 1, 0, Math.PI * 2, false);
        ctx.arc(this.x, this.y, this.radius + 2, 0, Math.PI * 2, false);
        ctx.arc(this.x, this.y, this.radius + 3, 0, Math.PI * 2, false);
        ctx.stroke();
        ctx.closePath();
      }
    };
  
    function createDots() {
      for (i = 0; i < dots.nb; i++) {
        dots.array.push(new Dot());
      }
      //dots.nb = 5;
    }
  
    function moveDots() {
      for (i = 0; i < dots.nb; i++) {
        var dot = dots.array[i];
  
        if (dot.y < 0 || dot.y > canvas.height) {
          dot.vx = dot.vx;
          dot.vy = -dot.vy;
        } else if (dot.x < 0 || dot.x > canvas.width) {
          dot.vx = -dot.vx;
          dot.vy = dot.vy;
        }
        dot.x += dot.vx;
        dot.y += dot.vy;
      }
    }
  
    var maxConnected = (dots.nbMax / 2).toFixed(1);
    function connectDots() {
      var connectionCount = 0;
      for (i = 0; i < dots.nb; i++) {
        for (j = 0; j < dots.nb; j++) {
          i_dot = dots.array[i];
          j_dot = dots.array[j];
  
          if (
            i_dot.x - j_dot.x < dots.distance &&
            i_dot.y - j_dot.y < dots.distance &&
            i_dot.x - j_dot.x > -dots.distance &&
            i_dot.y - j_dot.y > -dots.distance
          ) {
            if (
              i_dot.x - mousePosition.x < dots.d_radius &&
              i_dot.y - mousePosition.y < dots.d_radius &&
              i_dot.x - mousePosition.x > -dots.d_radius &&
              i_dot.y - mousePosition.y > -dots.d_radius
            ) {
              ctx.beginPath();
              ctx.strokeStyle = averageColorStyles(i_dot, j_dot);
              ctx.moveTo(i_dot.x, i_dot.y);
              ctx.lineTo(j_dot.x, j_dot.y);
              ctx.stroke();
              ctx.closePath();
  
              dots.array[i].drawBold();
              dots.array[j].drawBold();
              connectionCount++;
            }
          }
          if (connectionCount > maxConnected) return;
        }
      }
    }
  
    function drawDots() {
      for (i = 0; i < dots.nb; i++) {
        var dot = dots.array[i];
        dot.draw();
      }
    }
    var counter = 0;
    var moveMode = 1;
    var dotsMode = 1;
    var stepCounter = 0;
    var fps = 0,
      minFPS = 10000,
      maxFPS = 0,
      avgFPS = 0,
      now,
      lastUpdate = new Date() * 1,
      fpsFilter = 50;
    function animateDots() {
      //counter++;
      //if(counter >= 5)
      {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (dotsMode == 1) {
          maxConnected++;
          //        if(maxConnected%5 == 0)
          //         dots.d_radius++;
          if (maxConnected > dots.nbMax - 2) {
            dotsMode = 3;
            counter = 0;
          }
        } else if (dotsMode == 2) {
          maxConnected--;
          //        if(maxConnected%5 == 0)
          //          dots.d_radius--;
          if (maxConnected < 25) {
            dotsMode = 4;
            counter = 0;
          }
        } else if (dotsMode == 3) {
          //      if(counter % 30 == 0)
          //       dots.distance++;
          counter++;
          if (counter > 15) {
            counter = 0;
            dotsMode = 2;
          }
        } else if (dotsMode == 4) {
          counter++;
          //   dots.distance--;
          if (counter > 150) {
            counter = 0;
            dotsMode = 1;
          }
        }
        /*
        if(dotsMode == 1) {
          dots.nb++;
          if(dots.nb%5 == 0)
            dots.d_radius++;
          if(dots.nb > (dots.nbMax-2)) {
            dotsMode = 3;
            counter = 0;
          }
        }else if(dotsMode == 2) {
          dots.nb--;
          if(dots.nb%5 == 0)
            dots.d_radius--;
          if(dots.nb < 25) {
            dotsMode = 4;
            counter = 0;
          }
        }else if(dotsMode == 3) {
    //      if(counter % 30 == 0)
     //       dots.distance++;
          counter++;
          if(counter > 15) {
            counter = 0;
            dotsMode = 2;          
          }          
        }else if(dotsMode == 4) {
          counter++;
       //   dots.distance--;
          if(counter > 150) {
            counter = 0;
            dotsMode = 1;
          }          
        }
        */
  
        if (mousePosition.y < 0 || mousePosition.y > canvas.height) {
          mousePosition.vy = -mousePosition.vy;
        } else if (mousePosition.x < 0 || mousePosition.x > canvas.width) {
          mousePosition.vx = -mousePosition.vx;
        }
        mousePosition.x += mousePosition.vx;
        mousePosition.y += mousePosition.vy;
  
        /*      
        if(moveMode == 1) {
          mousePosition.x = (mousePosition.x + 2);
          if(mousePosition.x > (canvas.width-1))
            moveMode = 2;
        }else if(moveMode == 2) {
          mousePosition.y = (mousePosition.y+2);
          if(mousePosition.y > (canvas.height-1))
            moveMode = 3;
        }else if(moveMode == 3) {
          mousePosition.x = (mousePosition.x - 5);
          if(mousePosition.x < 1)
            moveMode = 4;
        }else if(moveMode == 4) {
          mousePosition.y = (mousePosition.y-5);
          if(mousePosition.y < 1)
            moveMode = 1;
        }
        */ moveDots();
        drawDots();
        connectDots();
  
        var thisFrameFPS = 1000 / ((now = new Date()) - lastUpdate);
        if (now != lastUpdate) {
          fps += (thisFrameFPS - fps) / fpsFilter;
          //avgFPS = (avgFPS + fps)/2;
          lastUpdate = now;
  
          if (fps < minFPS) {
            minFPS = fps;
            avgFPS = (minFPS + maxFPS) / 2;
          }
  
          if (fps > maxFPS) {
            maxFPS = fps;
            avgFPS = (minFPS + maxFPS) / 2;
          }
        }
      }
      requestAnimationFrame(animateDots);
    }
  
    /*  canvas.addEventListener('mousemove', function(e){
      mousePosition.x = e.pageX;
      mousePosition.y = e.pageY;    
    });
  
    canvas.addEventListener('mouseleave', function(e){
      mousePosition.x = canvas.width / 2;
      mousePosition.y = canvas.height / 2;
    });
  */
    createDots();
    window.addEventListener("resize", resizeCanvas, false);
    window.addEventListener("orientationchange", resizeCanvas, false);
    window.setInterval(updateFPS, 1000);
  
    var fpsCounter = 0;
    function updateFPS() {
      var FPS = document.querySelector("#FPS");
      FPS.innerHTML =
        "FPS:" +
        fps.toFixed(2) +
        ", MAX:" +
        maxFPS.toFixed(2) +
        ", MIN:" +
        minFPS.toFixed(2) +
        ", MEAN:" +
        avgFPS.toFixed(2) +
        ", MC:" +
        maxConnected.toFixed(0); // + ", NB:" + dots.nb+ " ," + dotsMode;
      if (fpsCounter++ > 15) {
        minFPS = fps;
        maxFPS = fps;
        fpsCounter = 0;
      }
    }
  
    function resizeCanvas() {
      var canvas = document.querySelector("canvas");
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    requestAnimationFrame(animateDots);
    updateFPS();
  })();
  