<script setup>
defineProps({ experiences: { type: Array, default: () => [] } })
</script>
<template>
  <div v-if="experiences.length" class="experience">
    <h3>工作经历</h3>
    <article v-for="entry in experiences" :key="entry.company + entry.period">
      <header>
        <p class="meta">{{ entry.period }}</p>
        <h4>{{ entry.company }}</h4>
        <p class="role">{{ entry.role }}</p>
      </header>
      <ul><li v-for="point in entry.points" :key="point">{{ point }}</li></ul>
    </article>
  </div>
</template>
<style scoped>
.experience { margin-top:64px; border-top:1px solid var(--line-strong); padding-top:32px; }
h3 { font-size:32px; margin:0 0 28px; }
article { display:grid; grid-template-columns:1fr 1.5fr; gap:48px; }
h4 { font-size:23px; line-height:1.5; margin:12px 0; }
.role { color:var(--vermilion); font-size:14px; }
ul { list-style:none; padding:0; margin:0; }
li { border-top:1px solid var(--line); padding:14px 0; font-size:15px; line-height:1.85; }
@media(max-width:800px) { article { grid-template-columns:1fr; gap:20px; } }
</style>
