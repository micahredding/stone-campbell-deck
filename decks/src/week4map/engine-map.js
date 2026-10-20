<script>
/* Map engine: the Chapter 3 engine's slides, frags, read/present modes, notes strip and
   presenter window, with the deck walked as a spine plus side paths instead of one line.
   → / space: next along the path you are on. ↓ or 1–3: take a side path from here.
   ↑: back to the spine slide the side path hangs from. m: the map (click any dot). */
(function(){
  var MAP=/*MAP*/null;
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  [].slice.call(document.querySelectorAll('[data-mirror]')).forEach(function(ph){
    var src=document.getElementById(ph.getAttribute('data-mirror'));
    if(!src){return}
    var c=src.cloneNode(true);
    c.removeAttribute('id');
    [].slice.call(c.querySelectorAll('[id]')).forEach(function(e){e.removeAttribute('id')});
    ph.parentNode.replaceChild(c,ph);
  });
  var bar=document.getElementById('bar'),count=document.getElementById('count'),hint=document.getElementById('hint');
  var strip=document.getElementById('strip'),modeEl=document.getElementById('mode'),pres=document.getElementById('pres');
  var doorsEl=document.getElementById('doors'),crumbEl=document.getElementById('crumb'),mapEl=document.getElementById('map');
  var q=new URLSearchParams(location.search);
  var LS={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
  var isPrev=q.has('preview'),isPres=q.has('presenter');
  if(isPrev||isPres)LS.set=function(){};

  /* ---- the map ---- */
  var spine=MAP.spine,branches=MAP.branches;
  var where=slides.map(function(){return null});           /* slide -> {b:-1|branch, k:position} */
  spine.forEach(function(s,k){where[s]={b:-1,k:k}});
  branches.forEach(function(br,b){br.slides.forEach(function(s,k){where[s]={b:b,k:k}})});
  var docs=MAP.docs||[],docDoors=MAP.docDoors||[],slideDoc=MAP.slideDoc||{};
  var docvEl=document.getElementById('docv'),ctxEl=document.getElementById('ctx');
  /* exits from a spine slide: side paths ({b}) and whole documents ({d}) */
  function exitsAt(i){var a=[];
    branches.forEach(function(br,b){if(br.fork===i)a.push({b:b})});
    docDoors.forEach(function(dd){if(dd.fork===i)a.push({d:dd.doc,label:dd.label})});return a}
  function exitLabel(x){return x.b!=null?branches[x.b].label:x.label}
  function exitSeen(x){return x.b!=null?branchSeen(x.b):!!seen['d'+x.d]}
  function takeExit(x){if(x.b!=null)goto(branches[x.b].slides[0],false);else openDoc(x.d,cur)}
  function pathOf(i){var w=where[i];return w.b<0?spine:branches[w.b].slides}
  /* where → goes from slide i: along the path; off the end of a side path, back to its fork */
  function nextOf(i){var w=where[i],p=pathOf(i);
    if(w.k<p.length-1)return p[w.k+1];
    return w.b<0?-1:branches[w.b].fork}
  function prevOf(i){var w=where[i],p=pathOf(i);
    if(w.k>0)return p[w.k-1];
    return w.b<0?-1:branches[w.b].fork}
  var seen={};try{seen=JSON.parse(LS.get('w4mseen')||'{}')||{}}catch(e){seen={}}
  function branchSeen(b){return branches[b].slides.some(function(s){return seen[s]})}

  var cur=0,interacted=false;
  function isPresent(){return document.body.classList.contains('present')}
  function fragsOf(i){var a=[].slice.call(slides[i].querySelectorAll('.frag')).filter(function(f){return !f.classList.contains('wp')&&!(isPresent()&&f.classList.contains('nt'))});a.sort(function(x,y){return (+(x.getAttribute('data-o')||0))-(+(y.getAttribute('data-o')||0))});return a}
  function syncWP(i){[].slice.call(slides[i].querySelectorAll('.wp')).forEach(function(w){
    var p=w.previousElementSibling,t=null;
    while(p){if(p.classList.contains('frag')&&!p.classList.contains('wp')&&!(isPresent()&&p.classList.contains('nt'))){t=p;break}p=p.previousElementSibling}
    w.classList.toggle('on',t?t.classList.contains('on'):true)})}
  function notesOf(i){var a=slides[i].querySelector('aside.notes');return a?a.innerHTML:''}
  function titleOf(i){return MAP.titles[i]||'—'}
  function doorHTML(i){return exitsAt(i).map(function(x,n){
      return '<div class="door'+(x.d!=null?' doc':'')+(exitSeen(x)?' seen':'')+'" data-x="'+n+'"><b>'+(n+1)+'</b>'+exitLabel(x)+'</div>'}).join('')}
  function render(){
    syncWP(cur);
    seen[cur]=1;LS.set('w4mseen',JSON.stringify(seen));
    slides.forEach(function(s,i){s.classList.toggle('on',i===cur)});
    var w=where[cur];
    if(w.b<0){count.textContent=(w.k+1)+' / '+spine.length;crumbEl.innerHTML='';
      bar.style.width=((w.k+1)/spine.length*100)+'%'}
    else{var br=branches[w.b];
      count.textContent='side '+(w.k+1)+' / '+br.slides.length;
      crumbEl.innerHTML='Side path &middot; <i>'+br.label+'</i> &middot; &uarr; back';
      bar.style.width=((where[br.fork].k+1)/spine.length*100)+'%'}
    /* doors show once the slide is fully built, so they never step on a reveal */
    var built=fragsOf(cur).every(function(f){return f.classList.contains('on')});
    doorsEl.innerHTML=built?doorHTML(cur):'';
    ctxEl.innerHTML=(built&&slideDoc[cur]!=null)?'<span>&#10530; in the document</span>':'';
    strip.innerHTML='<i>'+(cur+1)+'</i> &nbsp; '+notesOf(cur);
    var nx=nextOf(cur);
    LS.set('w4mcur',String(cur));LS.set('w4mnext',String(nx));
    LS.set('w4mdoors',JSON.stringify(exitsAt(cur).map(function(x){return [exitLabel(x),exitSeen(x)?1:0]})));
    try{history.replaceState(null,'',location.search+'#'+(cur+1))}catch(e){}
    if(document.body.classList.contains('mapon'))drawMap();
  }
  function setMode(m){
    document.body.classList.toggle('present',m==='present');LS.set('w4mmode',m);
    modeEl.textContent=(m==='present')?'present':'read';render();
  }
  function setStrip(on){document.body.classList.toggle('strip',!!on);LS.set('w4mstrip',on?'1':'0')}
  function goto(i,built){
    if(i<0||i>=slides.length)return;
    cur=i;fragsOf(cur).forEach(function(f){f.classList.toggle('on',!!built)});render();
  }
  function next(){
    interacted||fadeHint();
    var fr=fragsOf(cur);
    for(var i=0;i<fr.length;i++){if(!fr[i].classList.contains('on')){fr[i].classList.add('on');render();return}}
    var n=nextOf(cur);if(n>=0)goto(n,where[cur].b>=0&&n===branches[where[cur].b].fork);
  }
  function prev(){
    interacted||fadeHint();
    var fr=fragsOf(cur);
    for(var i=fr.length-1;i>=0;i--){if(fr[i].classList.contains('on')){fr[i].classList.remove('on');render();return}}
    var p=prevOf(cur);if(p>=0)goto(p,true);
  }
  function door(n){                     /* n = 0-based door index, or -1 for the first one not yet taken */
    var d=exitsAt(cur);if(!d.length)return;
    if(n<0){n=0;for(var k=0;k<d.length;k++){if(!exitSeen(d[k])){n=k;break}}}
    if(n>=d.length)return;
    takeExit(d[n]);
  }
  function up(){var w=where[cur];if(w.b>=0)goto(branches[w.b].fork,true)}
  function fadeHint(){interacted=true;hint.classList.add('gone')}
  function openPresenter(){window.open(location.href.split(/[?#]/)[0]+'?presenter=1','w4mpresenter','width=960,height=640')}
  function sharedCur(){var c=parseInt(LS.get('w4mcur')||'0',10);if(isNaN(c))c=0;return Math.max(0,Math.min(slides.length-1,c))}
  function sharedNext(){var c=parseInt(LS.get('w4mnext')||'-1',10);return isNaN(c)?-1:c}

  /* ---- the map overlay: spine left to right, side paths hanging below their fork ---- */
  function wrap(t,n){var w=t.split(' '),L=[],c='';w.forEach(function(x){if(c&&(c+' '+x).length>n){L.push(c);c=x}else c=c?c+' '+x:x});if(c)L.push(c);return L}
  function drawMap(){
    var W=1600,X0=50,X1=W-50,Y=96,DY=46,FAN=125,step=(X1-X0)/Math.max(1,spine.length-1);
    var depth=Math.max.apply(null,branches.map(function(b){return b.slides.length}).concat([1]));
    var H=Y+70+depth*DY+90+170,s=[],lastX=-1e9,lift=0;
    s.push('<svg viewBox="0 0 '+W+' '+H+'" xmlns="http://www.w3.org/2000/svg">');
    s.push('<line class=rail x1='+X0+' y1='+Y+' x2='+X1+' y2='+Y+' />');
    /* where every dot sits, so the sources' roots can be drawn first, under everything */
    var P={};spine.forEach(function(sl,k){P[sl]={x:X0+k*step,y:Y}});
    branches.forEach(function(br,b){var fx=X0+where[br.fork].k*step,sibs=exitsAt(br.fork),sib=sibs.map(function(x){return x.b}).indexOf(b);
      var x=Math.min(X1-40,Math.max(X0+40,fx+(sib-(sibs.length-1)/2)*FAN));br.slides.forEach(function(sl,k){P[sl]={x:x,y:Y+56+k*DY}})});
    /* sources row: each whole document sits under the stretch of the hour that quotes it,
       with a faint root up to every slide drawn from it */
    var YS=H-120;
    docs.forEach(function(D,di){
      var xs=[],sx=[];Object.keys(slideDoc).forEach(function(k){if(slideDoc[k]===di){xs.push(P[+k]);if(where[+k].b<0)sx.push(P[+k].x)}});
      if(!xs.length)return;
      var x=(sx.length?sx:xs.map(function(p){return p.x})).reduce(function(t,v){return t+v},0)/(sx.length||xs.length),ok=!!seen['d'+di];
      xs.forEach(function(p){s.push('<line class="root'+(ok?' seen':'')+'" x1='+x+' y1='+(YS-6)+' x2='+p.x+' y2='+(p.y+10)+' />')});
      s.push('<rect class="page'+(ok?' seen':'')+(docOpen===di?' cur':'')+'" x='+(x-17)+' y='+(YS-4)+' width=34 height=44 rx=2 data-d='+di+' />');
      for(var l=0;l<4;l++)s.push('<line class=pline x1='+(x-10)+' x2='+(x+10)+' y1='+(YS+6+l*8)+' y2='+(YS+6+l*8)+' />');
      var lab=docDoors.filter(function(dd){return dd.doc===di}).map(function(dd){return dd.label})[0]||D.title;
      s.push('<text class="blab src'+(ok?' seen':'')+'" text-anchor=middle x='+x+' y='+(YS+68)+'>'+lab.replace(/&rsquo;/g,'\u2019').replace(/, whole$/,'')+'</text>');
    });
    MAP.sections.forEach(function(sec){var x=X0+sec.at*step;
      lift=(x-lastX<150&&!lift)?26:0;lastX=x;   /* close neighbours take turns on two rows */
      s.push('<line class=twig x1='+x+' y1='+(Y-44-lift)+' x2='+x+' y2='+(Y-16)+' /><text class=sec x='+x+' y='+(Y-52-lift)+'>'+sec.label+'</text>')});
    branches.forEach(function(br,b){
      var fx=X0+where[br.fork].k*step,sibs=exitsAt(br.fork),sib=sibs.map(function(x){return x.b}).indexOf(b);
      var x=Math.min(X1-40,Math.max(X0+40,fx+(sib-(sibs.length-1)/2)*FAN)),ok=branchSeen(b);
      var y0=Y+56,yEnd=y0+(br.slides.length-1)*DY;
      s.push('<path class="twig'+(ok?' seen':'')+'" d="M'+fx+' '+Y+' L'+x+' '+y0+' L'+x+' '+yEnd+'" fill=none />');
      br.slides.forEach(function(sl,k){s.push(dot(x,y0+k*DY,sl,true))});
      s.push('<text class="blab'+(ok?' seen':'')+'" text-anchor=middle>'+wrap(br.label,14).map(function(l,k){
        return '<tspan x='+x+' y='+(yEnd+34+k*22)+'>'+l+'</tspan>'}).join('')+'</text>');
    });
    spine.forEach(function(sl,k){s.push(dot(X0+k*step,Y,sl,false))});
    s.push('</svg>');
    var nSide=branches.length,nSeen=branches.filter(function(b,i){return branchSeen(i)}).length;
    mapEl.innerHTML='<h3>Chapter 4 &middot; the map</h3><div class=mk>'+nSeen+' of '+nSide+
      ' side paths walked &middot; pages = whole documents &middot; filled = visited &middot; click any dot &middot; m or Esc to close &middot; r clears the trail</div>'+s.join('')+'<div class=tip id=maptip></div>';
  }
  function dot(x,y,sl,side){
    return '<circle class="dot'+(side?' side':'')+(seen[sl]?' seen':'')+(sl===cur?' cur':'')+'" cx='+x+' cy='+y+' r='+(sl===cur?12:8)+' data-s='+sl+' />';
  }
  function toggleMap(on){
    on=(on===undefined)?!document.body.classList.contains('mapon'):on;
    document.body.classList.toggle('mapon',on);if(on)drawMap();
  }
  mapEl.addEventListener('mouseover',function(e){var d=e.target.closest('.dot');var t=document.getElementById('maptip');
    var pg=e.target.closest('.page');
    if(t)t.innerHTML=d?((+d.getAttribute('data-s')+1)+' · '+titleOf(+d.getAttribute('data-s'))):(pg?docs[+pg.getAttribute('data-d')].title:'')});
  mapEl.addEventListener('click',function(e){e.stopPropagation();var d=e.target.closest('.dot');
    if(d){toggleMap(false);goto(+d.getAttribute('data-s'),false);return}
    var pg=e.target.closest('.page');if(pg){toggleMap(false);openDoc(+pg.getAttribute('data-d'))}});
  doorsEl.addEventListener('click',function(e){e.stopPropagation();var d=e.target.closest('.door');
    if(d){var x=exitsAt(cur)[+d.getAttribute('data-x')];if(x)takeExit(x)}});
  ctxEl.addEventListener('click',function(e){e.stopPropagation();zoomOut()});

  /* ---- whole documents: zoom out from a quote to its page, zoom in from any marked passage ---- */
  var docOpen=-1;
  function docOn(){return docOpen>=0}
  function openDoc(d,focus){
    docOpen=d;seen['d'+d]=1;LS.set('w4mseen',JSON.stringify(seen));LS.set('w4mdoc',String(d));
    var D=docs[d];
    docvEl.innerHTML='<div class=dhead><div class=eyebrow>The whole document</div><h3>'+D.title+'</h3><div class=dsub>'+D.sub+'</div>'+
      '<div class=dkey>Gold: quoted in tonight&rsquo;s slides &middot; filled = already shown &middot; click a passage to zoom in &middot; z or Esc: back to the slide</div></div>'+
      '<div class=dbody>'+D.html+'</div>';
    var here=null;
    [].slice.call(docvEl.querySelectorAll('mark')).forEach(function(m){
      var ss=m.getAttribute('data-s').split(' ').map(Number);
      if(ss.some(function(x){return seen[x]}))m.classList.add('seen');
      if(focus!=null&&ss.indexOf(focus)>=0){m.classList.add('here');here=here||m}
      m.title=ss.map(function(x){return 'slide '+(x+1)+' · '+titleOf(x)}).join('\n');
    });
    document.body.classList.add('docon');
    docvEl.scrollTop=0;
    if(here)docvEl.scrollTop=Math.max(0,here.offsetTop-docvEl.clientHeight*.38);
    if(document.body.classList.contains('mapon'))toggleMap(false);
  }
  function closeDoc(){docOpen=-1;LS.set('w4mdoc','-1');document.body.classList.remove('docon')}
  function zoomOut(){if(docOn()){closeDoc();return}var d=slideDoc[cur];if(d!=null)openDoc(d,cur)}
  docvEl.addEventListener('click',function(e){e.stopPropagation();var m=e.target.closest('mark');if(!m)return;
    var ss=m.getAttribute('data-s').split(' ').map(Number);
    var t=ss.indexOf(cur)>=0?cur:(ss.filter(function(x){return where[x].b<0})[0]);if(t==null)t=ss[0];
    closeDoc();goto(t,true)});

  /* ---- preview pane (?preview=1): NOW (off=0) or NEXT along the path (off=1) ---- */
  if(isPrev){
    document.body.classList.add('preview');
    var pvS=-1,pvM='',pvPushed=false,off=q.get('off')==='0'?0:1;
    function pvApply(c,n,m){
      var t=off?n:c;
      if(t<0){document.body.style.visibility='hidden';return}document.body.style.visibility='';
      if(t!==pvS||m!==pvM){pvS=t;pvM=m;document.body.classList.toggle('present',m==='present');
        cur=t;fragsOf(cur).forEach(function(f){f.classList.add('on')});syncWP(cur);
        slides.forEach(function(s,i){s.classList.toggle('on',i===cur)})}
    }
    window.addEventListener('message',function(e){var d=e.data;if(d&&d.w4m){pvPushed=true;pvApply(d.cur,d.next,d.mode||'present')}});
    function pvTick(){if(!pvPushed)pvApply(sharedCur(),sharedNext(),LS.get('w4mmode')||'present')}
    pvTick();setInterval(pvTick,200);window.addEventListener('storage',pvTick);
    return;
  }
  /* ---- presenter window (?presenter=1): notes, now, next along the path, doors here ---- */
  if(isPres){
    document.body.classList.add('presenter');
    var pbase=location.href.split(/[?#]/)[0];
    pres.innerHTML='<div class=pcol><div class=pn id=ppn></div><div class=pt id=ppt></div>'+
      '<div class=pnotes id=ppnotes></div></div>'+
      '<div class=pside><div class=plabel>NOW &middot; fully built</div>'+
      '<div class=pwrap id=ppwrap0><iframe id=ppif0 src="'+pbase+'?preview=1&off=0"></iframe></div>'+
      '<div class=plabel id=pplabel>NEXT</div>'+
      '<div class=pwrap id=ppwrap><iframe id=ppif src="'+pbase+'?preview=1&off=1"></iframe></div>'+
      '<div class=pnexttitle id=ppnt></div><div class=pdoors id=ppdoors></div>'+
      '<div class=pkeys>&rarr; next &middot; &darr; or 1&ndash;3 side path &middot; &uarr; back &middot; z document &middot; m map</div></div>';
    var ppif=document.getElementById('ppif'),ppwrap=document.getElementById('ppwrap');
    var ppif0=document.getElementById('ppif0'),ppwrap0=document.getElementById('ppwrap0');
    function pfit(){ppif.style.transform='scale('+(ppwrap.clientWidth/1920)+')';ppif0.style.transform='scale('+(ppwrap0.clientWidth/1920)+')'}
    pfit();window.addEventListener('resize',pfit);setTimeout(pfit,300);
    function ppush(){var m={w4m:1,cur:sharedCur(),next:sharedNext(),mode:LS.get('w4mmode')||'present'};
      [ppif,ppif0].forEach(function(f){try{f.contentWindow&&f.contentWindow.postMessage(m,'*')}catch(e){}})}
    ppif.addEventListener('load',ppush);ppif0.addEventListener('load',ppush);
    var lastKey='';
    function tick(){
      var c=sharedCur(),n=sharedNext(),dj=LS.get('w4mdoors')||'[]',dv=+(LS.get('w4mdoc')||'-1');ppush();
      var key=c+'|'+n+'|'+dj+'|'+dv;
      if(key!==lastKey){lastKey=key;
        var w=where[c];
        document.getElementById('ppn').textContent=w.b<0?('spine '+(w.k+1)+' / '+spine.length):('side path · '+branches[w.b].label+' · '+(w.k+1)+' / '+branches[w.b].slides.length);
        document.getElementById('ppt').innerHTML=dv>=0?('<span style="color:var(--bone)">ROOM SEES THE DOCUMENT:</span> '+docs[dv].title+' &middot; z to return'):titleOf(c).replace(/</g,'&lt;');
        document.getElementById('ppnotes').innerHTML=notesOf(c);
        var back=w.b>=0&&n===branches[w.b].fork;
        document.getElementById('pplabel').textContent=n<0?'END OF DECK':(back?'NEXT · back to the spine':'NEXT');
        ppwrap.style.visibility=n<0?'hidden':'visible';
        document.getElementById('ppnt').textContent=n<0?'':((n+1)+' · '+titleOf(n));
        var d=[];try{d=JSON.parse(dj)}catch(e){}
        document.getElementById('ppdoors').innerHTML=d.length?('SIDE PATHS HERE<br>'+d.map(function(x,k){return '<span class="'+(x[1]?'seen':'')+'"><b>'+(k+1)+'</b> '+x[0]+(x[1]?' ✓':'')+'</span>'}).join('<br>')):'';
      }
    }
    tick();setInterval(tick,200);window.addEventListener('storage',tick);
    var seq=0;
    function cmd(d){seq++;try{localStorage.setItem('w4mcmd',Date.now()+':'+seq+':'+d)}catch(e){}}
    document.addEventListener('keydown',function(e){
      if(e.metaKey||e.ctrlKey||e.altKey)return;
      switch(e.key){
        case 'ArrowRight':case ' ':case 'PageDown':e.preventDefault();cmd('next');break;
        case 'ArrowLeft':case 'Backspace':case 'PageUp':e.preventDefault();cmd('prev');break;
        case 'ArrowDown':e.preventDefault();cmd('door');break;
        case 'ArrowUp':e.preventDefault();cmd('up');break;
        case '1':case '2':case '3':case '4':cmd('door'+e.key);break;
        case 'm':case 'M':cmd('map');break;
        case 'Escape':cmd('mapoff');break;
        case 'z':case 'Z':cmd('zoom');break;
        case 'f':case 'F':
          if(document.fullscreenElement)document.exitFullscreen&&document.exitFullscreen();
          else document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen();
          break;
      }
    });
    return;
  }
  function run(c){
    if(c==='next')next();else if(c==='prev')prev();else if(c==='door')door(-1);
    else if(c==='up')up();else if(c==='map')toggleMap();else if(c==='mapoff')toggleMap(false);
    else if(c==='zoom')zoomOut();
    else if(c.slice(0,4)==='door')door(+c.slice(4)-1);
  }
  document.addEventListener('keydown',function(e){
    if(e.metaKey||e.ctrlKey||e.altKey)return;
    var mapOn=document.body.classList.contains('mapon');
    if(docOn()){if(e.key==='z'||e.key==='Z'||e.key==='Escape'){e.preventDefault();closeDoc()}
      else if(e.key==='m'||e.key==='M')toggleMap(true);
      else if(e.key==='f'||e.key==='F'){if(document.fullscreenElement)document.exitFullscreen&&document.exitFullscreen();else document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen()}
      return}
    switch(e.key){
      case 'z':case 'Z':if(!mapOn)zoomOut();break;
      case 'ArrowRight':case ' ':case 'PageDown':e.preventDefault();if(!mapOn)next();break;
      case 'ArrowLeft':case 'Backspace':case 'PageUp':e.preventDefault();if(!mapOn)prev();break;
      case 'ArrowDown':e.preventDefault();if(!mapOn)door(-1);break;
      case 'ArrowUp':e.preventDefault();if(!mapOn)up();break;
      case '1':case '2':case '3':case '4':if(!mapOn)door(+e.key-1);break;
      case 'm':case 'M':toggleMap();break;
      case 'Escape':toggleMap(false);break;
      case 'r':case 'R':if(mapOn){seen={};LS.set('w4mseen','{}');render()}break;
      case 'Home':goto(spine[0],false);break;
      case 'End':goto(spine[spine.length-1],true);break;
      case 'n':case 'N':setMode(isPresent()?'read':'present');break;
      case 's':case 'S':setStrip(!document.body.classList.contains('strip'));break;
      case 'p':case 'P':openPresenter();break;
      case 'f':case 'F':
        if(document.fullscreenElement)document.exitFullscreen&&document.exitFullscreen();
        else document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen();
        break;
    }
  });
  document.addEventListener('click',function(e){
    if(e.target.closest('#strip')||document.body.classList.contains('mapon')||docOn())return;
    (e.clientX<innerWidth/5)?prev():next()});
  var tx=null,ty=null;
  document.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;ty=e.touches[0].clientY},{passive:true});
  document.addEventListener('touchend',function(e){
    if(tx==null||docOn()||document.body.classList.contains('mapon')){tx=null;return}var dx=e.changedTouches[0].clientX-tx,dy=e.changedTouches[0].clientY-ty;tx=ty=null;
    if(Math.abs(dy)>Math.abs(dx)){if(dy<-40)door(-1);else if(dy>40)up();return}
    if(dx<-40)next();else if(dx>40)prev();
  },{passive:true});
  var h=parseInt((location.hash||'').replace('#',''),10);
  if(h>=1&&h<=slides.length)cur=h-1;
  var lastCmd=LS.get('w4mcmd')||'';
  setInterval(function(){
    var v=LS.get('w4mcmd')||'';
    if(v&&v!==lastCmd){lastCmd=v;run(v.split(':').slice(2).join(':'))}
  },200);
  setStrip((LS.get('w4mstrip')||'0')==='1');
  setMode(q.get('mode')||LS.get('w4mmode')||'present');
  fragsOf(cur).forEach(function(f){f.classList.remove('on')});render();
  setTimeout(fadeHint,8000);
})();
</script>
