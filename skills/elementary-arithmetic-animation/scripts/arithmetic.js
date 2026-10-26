/* Deterministic teaching states. Shared by browser and Node verification. */
(function(root){
function solve(a,b,op){
 if(!Number.isInteger(a)||!Number.isInteger(b)||a<0||b<0||a>9999||b>9999)throw Error('请输入 0—9999 之间的整数');
 if(!['+','-','*','/'].includes(op))throw Error('请选择运算符');
 if(op==='-'&&a<b)throw Error('本版减法请让第一个数大于或等于第二个数');
 if(op==='/'&&b===0)throw Error('除数不能为 0');
 const steps=[], rows=[],marks={}; let hot=[],focus='',equation='',blocks=null;
 const digits=(v)=>String(v).split('').reverse().map(Number);
 const A=digits(a),B=digits(b),n=Math.max(A.length,B.length);
 function add(title,text){steps.push(JSON.parse(JSON.stringify({title,text,rows,marks,hot,focus,equation,blocks})));}
 function row(id,value,y,offset=0){const r={id,cells:{},y};String(value).split('').reverse().forEach((d,i)=>r.cells[i+offset]=d);rows.push(r);return r;}
 function mark(col,text){marks[col]=String(text);}
 if(op!=='/'){
 row('a',a,150);row('b',b,230);const out={id:'answer',cells:{},y:330};rows.push(out);
 add('先把数位对齐','个位对个位，十位对十位。'+(op==='*'?'依次计算每一行部分积。':'从个位开始计算。'));
 if(op==='+'){
 let carry=0;for(let i=0;i<n||carry;i++){
 const x=A[i]||0,y=B[i]||0,total=x+y+carry;hot=[i];equation=`${x} + ${y}${carry?' + '+carry:''} = ${total}`;
 blocks={kind:'count',col:i,low:total,high:0};
 add('计算'+place(i),`把这一位的数字${carry?'和进来的 1 ':''}相加。`);
 blocks={kind:total>=10?'merge':'count',col:i,low:total,high:0};
 out.cells[i]=String(total%10);carry=Math.floor(total/10);if(carry)mark(i+1,carry);focus=`answer:${i}`;
 add(carry?'写数，再进位':'写下这一位',carry?`${total} 个${unit(i)}，留下 ${total%10} 个${unit(i)}，向前一位进 1。`:`在${place(i)}写 ${total%10}。`);
 }
 }else if(op==='-'){
 const work=Array.from({length:n},(_,i)=>A[i]||0);
 for(let i=0;i<n;i++){
 hot=[i];const y=B[i]||0;
 if(work[i]<y){let k=i+1;while(work[k]===0)k++;
 blocks={kind:'split',col:k-1,high:work[k],low:work[k-1]};
 work[k]--;mark(k,work[k]);hot=[k,k-1];equation='1 个'+unit(k)+' = 10 个'+unit(k-1);
 add('向高位退 1',`${place(i)}不够减，先从${place(k)}退 1。`);
 for(let j=k-1;j>i;j--){blocks={kind:'split',col:j-1,high:10,low:work[j-1]};work[j]=9;mark(j,9);hot=[j,j-1];equation='10 − 1 = 9';add('经过零，继续退位',`${place(j)}得到 10，再向右退 1，剩下 9。`);}
 work[i]+=10;blocks={kind:'count',col:i,high:0,low:work[i]};mark(i,work[i]);hot=[i];equation=`${work[i]} − ${y}`;add('这一位得到 10',`${place(i)}现在是 ${work[i]}，可以继续相减。`);
 }
 blocks={kind:'remove',col:i,high:0,low:work[i],remove:y};
 const result=work[i]-y;equation=`${work[i]} − ${y} = ${result}`;out.cells[i]=String(result);focus=`answer:${i}`;add('计算'+place(i),`在${place(i)}写 ${result}。`);
 }
 }else{
 rows.pop();const partials=[];
 for(let j=0;j<B.length;j++){
 const p={id:'part'+j,cells:{},y:330+j*80};rows.push(p);let carry=0;
 for(let i=0;i<A.length;i++){
 const total=A[i]*B[j]+carry;hot=[i+j];equation=`${A[i]} × ${B[j]}${carry?' + '+carry:''} = ${total}`;
 add('计算第 '+(j+1)+' 行',`用乘数${place(j)}的 ${B[j]}，乘被乘数${place(i)}的 ${A[i]}。`);
 p.cells[i+j]=String(total%10);carry=Math.floor(total/10);if(carry)mark(i+j+1,carry);else delete marks[i+j+1];focus=`${p.id}:${i+j}`;
 add(carry?'写数并进位':'写下乘积',`写 ${total%10}${carry?'，向前一位进 '+carry:''}。`);
 }
 if(carry)p.cells[A.length+j]=String(carry);
 for(let z=0;z<j;z++)p.cells[z]='0';
 Object.keys(marks).forEach(k=>delete marks[k]);partials.push(a*B[j]*10**j);equation=String(partials[j]);add('完成这一行部分积',j?`乘的是${unit(j)}，这一行向左移动 ${j} 位；末尾的 0 用浅色补出数值。`:'完成个位乘法。');
 }
 const answer={id:'answer',cells:{},y:350+B.length*80};rows.push(answer);
 let sumCarry=0;const width=String(a*b).length;
 for(let col=0;col<width;col++){
 const values=partials.map(v=>Math.floor(v/10**col)%10),total=values.reduce((x,y)=>x+y,0)+sumCarry;
 hot=[col];equation=values.join(' + ')+(sumCarry?' + '+sumCarry:'')+' = '+total;
 add('部分积相加：'+place(col),'将各行相同数位的数字相加'+(sumCarry?'，加上进位。':'。'));
 answer.cells[col]=String(total%10);sumCarry=Math.floor(total/10);if(sumCarry)mark(col+1,sumCarry);
 focus=`answer:${col}`;add(sumCarry?'写数并进位':'写下这一位',`在${place(col)}写 ${total%10}`+(sumCarry?`，向前一位进 ${sumCarry}。`:'。'));
 }

 }
 }else{
 row('dividend',a,150);const q={id:'quotient',cells:{},y:70};rows.push(q);add('从高位开始除','从被除数左边开始，按“除、乘、减、落”逐步计算。');
 const ds=String(a).split('');let remainder=0,started=false,round=0;
 for(let i=0;i<ds.length;i++){
 const col=ds.length-1-i,current=remainder*10+Number(ds[i]);hot=[col];equation=`${remainder} × 10 + ${ds[i]} = ${current}`;
 add(i?'落下一位':'取出最高位',i?`把 ${ds[i]} 落下来，和前面的余数合成 ${current}。`:`先看 ${current}。`);
 if(current<b&&!started&&i<ds.length-1){remainder=current;equation=`${current} < ${b}`;add('还不够除','再看下一位，合起来继续除。');continue;}
 const digit=Math.floor(current/b),product=digit*b;started=true;q.cells[col]=String(digit);focus=`quotient:${col}`;equation=`${current} ÷ ${b} → 商 ${digit}`;add('在对应数位写商',digit===0?'这一位不够除，要在商中写 0 占位。':`试商 ${digit}：${b} × ${digit} = ${product}，不超过 ${current}。`);
 row('product'+round,product,230+round*155,col);equation=`${b} × ${digit} = ${product}`;add('乘：写出乘积','把除数与这一位的商相乘，乘积写在当前被除部分下面。');
 remainder=current-product;row('remainder'+round,remainder,295+round*155,col);equation=`${current} − ${product} = ${remainder}`;add('减：求出余数',`余数是 ${remainder}，小于除数 ${b}。`);round++;
 }
 }
 const answer=rows.find(r=>r.id==='answer');
 if(answer){const cols=Object.keys(answer.cells).map(Number).sort((x,y)=>y-x);for(const c of cols){if(c>0&&answer.cells[c]==='0')delete answer.cells[c];else break;}}
 blocks=null;hot=[];focus='';const result=op==='+'?a+b:op==='-'?a-b:op==='*'?a*b:Math.floor(a/b);equation=`${a} ${symbol(op)} ${b} = ${result}`+(op==='/'&&a%b?' … '+a%b:'');
 add('计算完成',op==='/'?`验算：${b} × ${result} + ${a%b} = ${a}。`:'回看每一位，检查数位对齐和进退位标记。');
 return {a,b,op,result,remainder:op==='/'?a%b:0,steps};
}
function place(i){return ['个位','十位','百位','千位','万位','十万位','百万位','千万位'][i]||`第 ${i+1} 位`;}
function unit(i){return ['一','十','百','千','万','十万','百万','千万'][i]||`10 的 ${i} 次方`;}
function symbol(op){return {'+':'+','-':'−','*':'×','/':'÷'}[op];}
root.Arithmetic={solve,place,symbol};if(typeof module!=='undefined')module.exports=root.Arithmetic;
})(typeof window!=='undefined'?window:globalThis);
