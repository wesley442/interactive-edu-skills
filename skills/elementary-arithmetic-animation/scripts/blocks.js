/* Adjacent-place base-ten exchanges, driven exclusively by solver snapshots. */
function renderBlocks(step){
 if(blockTimeline){blockTimeline.kill();blockTimeline=null;}
 const model=step.blocks,svg=$('blocks'),caption=$('blockCaption'),empty=$('blockEmpty');
 $('blockReplay').disabled=!model;
 svg.style.display=model?'block':'none';caption.hidden=!model;empty.hidden=!!model;
 if(!model){svg.innerHTML='';$('blockUnit').textContent='十进制 · 拆开与合并';empty.textContent=lesson.op==='*'||lesson.op==='/'?'积木拆合用于加减法的进退位；当前运算请跟随上方竖式学习。':'从个位开始，跟随每一步看积木如何合成、拆开和拿走。';return;}
 const {kind,col,high,low}=model,lower=10**col,upper=lower*10;
 $('blockUnit').textContent=`只看${Arithmetic.place(col+1)}与${Arithmetic.place(col)}`;
 const finalHigh=kind==='split'?high-1:kind==='merge'?high+1:high;
 const finalLow=kind==='split'?low+10:kind==='merge'?low-10:kind==='remove'?low-model.remove:low;
 caption.textContent=kind==='split'?`把 1 个 ${upper} 拆成 10 个 ${lower}，总量不变。`:kind==='merge'?`把 10 个 ${lower} 合成 1 个 ${upper}，剩下 ${finalLow} 个 ${lower}。`:kind==='remove'?`原有 ${low} 个 ${lower}，拿走 ${model.remove} 个，剩下 ${finalLow} 个。`:`这里有 ${low} 个 ${lower}，每一小块代表 ${lower}。`;
 const phone=matchMedia('(max-width:600px)').matches;svg.setAttribute('viewBox',phone?'0 0 340 400':'0 0 680 230');
 const lowPos=i=>({x:(phone?29:370)+(i%10)*(phone?29:25),y:(phone?260:70)+Math.floor(i/10)*38});
 const highPos=(i,j)=>({x:35+i*23,y:63+j*9});
 const square=(id,pos,color,size=18)=>`<rect id="${id}" x="${pos.x}" y="${pos.y}" width="${size}" height="${size}" rx="2" fill="${color}" stroke="#c3fff455" stroke-width="1"/>`;
 const highBox=phone?'15 40 310 120':'15 40 280 145';
 const lowBox=phone?'15 230 310 110':'345 40 320 145';
 const box=(coords,fill)=>{const [x,y,w,h]=coords.split(' ');return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="12" fill="${fill}"/>`;};
 let markup=box(highBox,'#ffbd740b')+box(lowBox,'#64f5c10a')+`<text x="30" y="25" font-size="13" fill="#ffcd91">${Arithmetic.place(col+1)} · 每根代表 ${upper}</text><text x="${phone?30:360}" y="${phone?215:25}" font-size="13" fill="#97f9d6">${Arithmetic.place(col)} · 每块代表 ${lower}</text><text x="${phone?306:314}" y="${phone?204:110}" text-anchor="middle" font-size="25" fill="#9db7cd">${kind==='merge'?(phone?'↑':'←'):kind==='split'?(phone?'↓':'→'):'·'}</text>`;
 for(let i=0;i<high;i++){
 if(kind==='split'&&i===high-1)continue;
 for(let j=0;j<10;j++)markup+=square(`rod-${i}-${j}`,highPos(i,j),'#ffc079',9);
 }
 for(let i=0;i<low;i++)markup+=square(`cube-${i}`,lowPos(i),'#67edc1');
 if(kind==='split')for(let j=0;j<10;j++)markup+=square(`exchange-${j}`,highPos(high-1,j),'#ffc079',9);
 markup+=`<text id="highCount" x="30" y="${phone?180:211}" font-size="14" fill="#ffcd91">${high} 根 × ${upper}</text><text id="lowCount" x="${phone?30:360}" y="${phone?371:211}" font-size="14" fill="#97f9d6">${low} 块 × ${lower}</text>`;
 svg.innerHTML=markup;svg.setAttribute('aria-label',caption.textContent);
 const finish=()=>{$('highCount').textContent=`${finalHigh} 根 × ${upper}`;$('lowCount').textContent=`${finalLow} 块 × ${lower}`;};
 const speed=Number($('speed').value),reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
 blockTimeline=gsap.timeline({onComplete:finish});
 if(kind==='split'){
 for(let j=0;j<10;j++){const dest=lowPos(low+j);blockTimeline.to($(`exchange-${j}`),{attr:{x:dest.x,y:dest.y,width:18,height:18},fill:'#67edc1',duration:1.2,ease:'power2.inOut'},.25+j*.055);}
 }else if(kind==='merge'){
 for(let j=0;j<10;j++){const dest=highPos(high,j);blockTimeline.to($(`cube-${j}`),{attr:{x:dest.x,y:dest.y,width:9,height:9},fill:'#ffc079',duration:1.2,ease:'power2.inOut'},.25+j*.055);}
 for(let i=10;i<low;i++){const dest=lowPos(i-10);blockTimeline.to($(`cube-${i}`),{attr:{x:dest.x,y:dest.y},duration:.7},1.5);}
 }else if(kind==='remove'){
 for(let i=finalLow;i<low;i++)blockTimeline.to($(`cube-${i}`),{fill:'#ff917d',duration:.25},.2).to($(`cube-${i}`),{opacity:0,y:25,duration:.8},.7+(i-finalLow)*.04);
 }else blockTimeline.from(svg.querySelectorAll('rect[id]'),{opacity:0,duration:.45,stagger:.018});
 blockTimeline.timeScale(speed);
 if(reduced)blockTimeline.progress(1);
}
