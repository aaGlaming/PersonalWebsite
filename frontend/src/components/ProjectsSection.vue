<script setup>
import { ref, onMounted } from 'vue'
import { getProjects } from '../api'

const projects = ref([])

onMounted(async () => {
  projects.value = await getProjects().catch(() => [])
})
</script>

<template>
  <section id="projects" class="art-section">
    <div class="art-container">
      <header class="head">
        <p class="meta">03 — Selected works</p>
        <h2>作品</h2>
      </header>
      <p class="lede">
        前两件为近期可演示应用；末两件为竞赛与课程系统档案。
      </p>
      <hr class="rule" />

      <article v-for="p in projects" :key="p.id" class="work">
        <h3>{{ p.name }}</h3>
        <p class="summary">{{ p.summary }}</p>
        <ul>
          <li v-for="(pt, j) in p.points" :key="j">{{ pt }}</li>
        </ul>
        <div class="foot">
          <div class="tags">
            <span v-for="t in p.tags" :key="t" class="tag">{{ t }}</span>
          </div>
          <a
            v-if="p.url"
            class="art-link"
            :href="p.url"
            target="_blank"
            rel="noopener noreferrer"
          >
            View archive <span class="arrow">→</span>
          </a>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 12px;
}
h2 {
  margin: 0;
  font-size: clamp(48px, 7vw, 92px);
}
.lede {
  margin: 0 0 28px;
  max-width: 46ch;
  color: var(--warm-gray);
  font-size: 15px;
}
.work {
  padding: 56px 0;
  border-bottom: 1px solid var(--line-strong);
}
h3 {
  margin: 0 0 16px;
  font-size: clamp(32px, 4vw, 48px);
  max-width: none;
}
.summary {
  margin: 0 0 22px;
  font-size: 17px;
  line-height: 1.7;
  max-width: 72ch;
}
ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
li {
  position: relative;
  padding: 12px 0 12px 18px;
  font-size: 15px;
  line-height: 1.75;
  color: color-mix(in srgb, var(--charcoal) 82%, transparent);
  border-top: 1px solid var(--line);
}
li:last-child {
  border-bottom: 1px solid var(--line);
}
li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 22px;
  width: 7px;
  height: 1px;
  background: var(--vermilion);
}
.foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px 24px;
  margin-top: 24px;
}
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 12px 18px;
}
.tag {
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--warm-gray);
}
</style>
