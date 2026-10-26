const assert=require('node:assert/strict');
const {solve}=require('../skills/elementary-arithmetic-animation/scripts/arithmetic.js');
const value=r=>Object.entries(r.cells).reduce((sum,[c,d])=>sum+Number(d)*10**Number(c),0);
let count=0;
function check(a,b,op){
 const l=solve(a,b,op),expected=op==='+'?a+b:op==='-'?a-b:op==='*'?a*b:Math.floor(a/b);
 assert.equal(l.result,expected);
 const end=l.steps.at(-1),answer=end.rows.find(r=>r.id===(op==='/'?'quotient':'answer'));
 assert.equal(value(answer),expected,`${a}${op}${b}: displayed answer`);
 if(op==='/') {assert.equal(l.result*b+l.remainder,a);assert(l.remainder<b);}
 for(const step of l.steps){
 const m=step.blocks;if(!m)continue;
 assert(m.low>=0&&m.low<=19);assert(m.high>=0&&m.high<=10);
 const before=m.high*10+m.low;
 if(m.kind==='merge'){assert(m.low>=10);assert.equal((m.high+1)*10+m.low-10,before);}
 if(m.kind==='split'){assert(m.high>0);assert.equal((m.high-1)*10+m.low+10,before);}
 if(m.kind==='remove')assert(m.remove<=m.low&&m.remove>=0);
 }
 for(const step of l.steps)for(const r of step.rows)for(const d of Object.values(r.cells))assert.match(d,/^\d$/);
 if(op==='*'){const ps=end.rows.filter(r=>r.id.startsWith('part'));assert.equal(ps.reduce((s,r)=>s+value(r),0),expected);}
 count++;
}
for(const [a,b,op] of [[999,1,'+'],[1000,586,'-'],[1000,1,'-'],[48,27,'*'],[306,20,'*'],[1005,5,'/'],[17,5,'/'],[3,8,'/'],[0,7,'/'],[9999,9999,'*']])check(a,b,op);
let seed=42;function random(){seed=(1664525*seed+1013904223)>>>0;return seed%10000;}
for(let i=0;i<500;i++){const a=random(),b=random();check(a,b,'+');check(Math.max(a,b),Math.min(a,b),'-');check(a,b,'*');check(a,b||1,'/');}
assert.throws(()=>solve(8,0,'/'));assert.throws(()=>solve(3,8,'-'));assert.throws(()=>solve(1.5,2,'+'));assert.throws(()=>solve(10000,1,'+'));
const borrow=solve(1000,586,'-');assert(borrow.steps.some(s=>s.marks[2]==='9'));assert(borrow.steps.some(s=>s.marks[1]==='9'));assert(borrow.steps.some(s=>s.marks[0]==='10'));
console.log(`PASS: ${count} arithmetic lessons, displayed answers, partial sums, division invariants and input boundaries`);

assert.equal(solve(8,6,'+').steps.find(s=>s.blocks?.kind==='merge').blocks.low,14);
assert.deepEqual(solve(1000,586,'-').steps.filter(s=>s.blocks?.kind==='split').map(s=>s.blocks.col),[2,1,0]);
