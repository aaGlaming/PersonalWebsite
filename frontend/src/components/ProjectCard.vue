<script setup>
defineProps({
  project: { type: Object, required: true },
  index: { type: Number, required: true },
  compact: { type: Boolean, default: false },
})
</script>

<template>
  <article :id="project.id" class="work" :class="{ compact }" :aria-labelledby="project.id + '-title'">
    <div class="meta metadata">
      <span>PROJECT / {{ String(index).padStart(2, '0') }}</span>
      <span>{{ project.period }}</span>
      <span>{{ project.role }}<template v-if="project.team"> · {{ project.team }}</template></span>
    </div>
    <h3 :id="project.id + '-title'">{{ project.name }}</h3>
    <p class="summary">{{ project.summary }}</p>
    <p v-if="project.scope" class="scope">{{ project.scope }}</p>
    <ol v-if="project.workflow" class="workflow" aria-label="项目主流程">
      <li v-for="(step, i) in project.workflow" :key="step">
        <span>{{ String(i + 1).padStart(2, '0') }}</span>{{ step }}
      </li>
    </ol>
    <div v-if="!compact" class="body">
      <div>
        <h4>我的工作</h4>
        <ul class="contributions">
          <li v-for="point in project.points" :key="point">{{ point }}</li>
        </ul>
      </div>
    </div>
    <details>
      <summary>{{ compact ? '查看项目细节' : '查看流程机制与技术栈' }}</summary>
      <ul v-if="compact" class="contributions">
        <li v-for="point in project.points" :key="point">{{ point }}</li>
      </ul>
      <div v-else class="mechanisms">
        <section v-for="mechanism in project.mechanisms" :key="mechanism.title">
          <h4>{{ mechanism.title }}</h4><p>{{ mechanism.body }}</p>
        </section>
      </div>
      <p class="stack"><strong>技术栈</strong> {{ project.medium }}</p>
    </details>
    <footer class="foot">
      <div class="tags"><span v-for="tag in project.tags" :key="tag">{{ tag }}</span></div>
      <a v-if="project.url" class="art-link" :href="project.url" target="_blank" rel="noopener noreferrer" :aria-label="project.name + '：打开项目链接'">
        {{ project.url.includes('github.com') ? '查看代码' : '访问网站' }} <span class="arrow">↗</span>
      </a>
    </footer>
  </article>
</template>

<style scoped>
.work { padding:52px 0; border-bottom:1px solid var(--line-strong); scroll-margin-top:90px; overflow-wrap:anywhere; }
.metadata { display:flex; flex-wrap:wrap; gap:12px 28px; margin-bottom:20px; }
h3 { margin:0 0 20px; font-size:clamp(30px,3.7vw,48px); }
.summary { margin:0 0 20px; max-width:76ch; font-size:17px; line-height:1.8; }
.scope { border-left:3px solid var(--vermilion); padding:10px 16px; font-size:15px; margin:24px 0; background:color-mix(in srgb,var(--vermilion) 5%,transparent); }
.workflow { list-style:none; display:grid; grid-template-columns:repeat(6,minmax(0,1fr)); margin:28px 0 36px; padding:0; border:1px solid var(--line); }
.workflow li { position:relative; padding:16px 12px; font-size:14px; }
.workflow li + li { border-left:1px solid var(--line); }
.workflow li:not(:last-child)::after { content:'→'; position:absolute; right:-7px; top:50%; color:var(--vermilion); background:var(--paper); z-index:1; }
.workflow span { display:block; font-size:10px; color:var(--vermilion); margin-bottom:8px; letter-spacing:.15em; }
.body { max-width:100%; }
h4 { font-size:18px; margin:0 0 16px; }
.contributions { list-style:none; padding:0; margin:0; }
.contributions li { border-top:1px solid var(--line); padding:14px 0; font-size:15px; line-height:1.85; }
details { border-top:1px solid var(--line); border-bottom:1px solid var(--line); margin-top:28px; }
summary { cursor:pointer; padding:18px 0; font-size:14px; }
summary:hover { color:var(--vermilion); }
.mechanisms { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:28px; padding-top:12px; }
.mechanisms h4 { font-size:16px; margin-bottom:8px; }
.mechanisms p,.stack { font-size:14px; line-height:1.85; color:var(--warm-gray); }
.stack { padding:16px 0; margin:0; }
.stack strong { color:var(--charcoal); margin-right:12px; }
.foot { display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:20px; margin-top:24px; }
.tags { display:flex; flex-wrap:wrap; gap:10px 18px; }
.tags span { font-size:11px; color:var(--warm-gray); }
.compact { padding:36px 0; }
.compact h3 { font-size:clamp(28px,3vw,38px); }
@media(max-width:800px) {
  .workflow { grid-template-columns:repeat(3,minmax(0,1fr)); }
  .workflow li:nth-child(4) { border-left:0; }
  .workflow li:nth-child(n+4) { border-top:1px solid var(--line); }
  .workflow li:nth-child(3)::after { content:none; }
  .mechanisms { grid-template-columns:1fr; gap:12px; }
}
@media(max-width:400px) {
  .metadata { gap:8px 14px; }
  .workflow li { padding:14px 8px; font-size:13px; }
}
</style>
