(function(){var b=document.body,m=document.getElementById('menu'),s=document.getElementById('scrim');
function t(o){b.classList.toggle('open',o)}
if(m)m.onclick=function(){t(!b.classList.contains('open'))};
if(s)s.onclick=function(){t(false)};
document.querySelectorAll('nav.side a').forEach(function(a){a.addEventListener('click',function(){t(false)})});
var c=document.querySelector('nav.side a.cur');if(c){var n=document.querySelector('nav.side');n.scrollTop=c.offsetTop-80}
var links={};document.querySelectorAll('nav.side .pp a').forEach(function(a){var h=a.getAttribute('href');if(h.charAt(0)==='#')links[h.slice(1)]=a});
if('IntersectionObserver' in window){var cur=null;var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var a=links[e.target.id];if(a){if(cur)cur.classList.remove('cur');a.classList.add('cur');cur=a}}})},{rootMargin:'-60px 0px -75% 0px'});
document.querySelectorAll('h3.paper').forEach(function(h){io.observe(h)})}
})();
