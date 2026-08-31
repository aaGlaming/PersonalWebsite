<script setup>
import { ref, onMounted } from 'vue'
import { getProjects } from '../api'

const projects = ref([])

onMounted(async () => {
  projects.value = await getProjects().catch(() => [])
})
</script>

<template>
  <section id="projects" class="hd-section">
    <div class="hd-container">
      <div class="hd-section-title">
        <h2>项目经历</h2>
        <svg class="squiggle" viewBox="0 0 120 20" fill="none">
          <path
            d="M4 12 C 20 4, 32 18, 48 11 C 64 4, 78 18, 94 11 C 104 7, 110 9, 116 10"
            stroke="#ff4d4d" stroke-width="3" stroke-linecap="round"
          />
        </svg>
      </div>

      <div class="grid">
        <article
          v-for="(p, i) in projects"
          :key="p.id"
          class="project"
          :class="{ featured: p.featured }"
          :style="{ transform: `rotate(${[1, -1.2, -0.8, 1.4][i % 4]}deg)` }"
        >
          <span v-if="p.featured" class="hd-tape"></span>
          <span v-else class="hd-tack"></span>

          <header>
            <h3>{{ p.name }}</h3>
            <div class="meta">
              <span class="role" :class="p.role === '负责人' ? 'lead' : 'member'">
                {{ p.role }}
              </span>
              <span class="period">{{ p.period }}</span>
            </div>
          </header>

          <p class="summary">{{ p.summary }}</p>

          <ul>
            <li v-for="(pt, j) in p.points" :key="j">{{ pt }}</li>
          </ul>

          <div class="tags">
            <el-tag v-for="t in p.tags" :key="t" size="large">{{ t }}</el-tag>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
}
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
.project {
  position: relative;
  background: #fff;
  border: 2.5px solid var(--hd-border);
  border-radius: var(--wobbly-md);
  box-shadow: var(--shadow-sm);
  padding: 34px 26px 24px;
  transition: transform 0.1s ease, box-shadow 0.1s ease;
}
.project:hover {
  transform: rotate(0deg) translateY(-3px) !important;
  box-shadow: var(--shadow);
}
.project.featured {
  background: var(--hd-postit);
}
.featured-badge {
  position: absolute;
  top: 10px;
  right: 14px;
  font-family: var(--font-marker);
  font-size: 14px;
  color: var(--hd-accent);
  transform: rotate(6deg);
}
header h3 {
  margin: 0 0 6px;
  font-size: 24px;
}
.meta {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 10px;
}
.role {
  display: inline-block;
  font-size: 14px;
  font-weight: 700;
  padding: 0 12px;
  border: 2px solid var(--hd-border);
  border-radius: var(--wobbly-sm);
}
.role.lead {
  background: var(--hd-accent);
  color: #fff;
}
.role.member {
  background: var(--hd-muted);
}
.period {
  font-family: var(--font-hand);
  color: var(--hd-blue);
  font-size: 16px;
}
.summary {
  margin: 0 0 12px;
  font-size: 16px;
  color: rgba(45, 45, 45, 0.8);
}
ul {
  margin: 0 0 16px;
  padding-left: 22px;
}
li {
  font-size: 15px;
  line-height: 1.75;
  margin-bottom: 4px;
}
li::marker {
  color: var(--hd-accent);
}
.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.tags .el-tag {
  background: #fff;
  color: var(--hd-fg);
}
.featured .tags .el-tag {
  background: #fff;
}
</style>
