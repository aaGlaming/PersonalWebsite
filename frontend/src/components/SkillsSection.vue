<script setup>
import { ref, onMounted } from 'vue'
import { getSkills } from '../api'

const skills = ref([])

onMounted(async () => {
  skills.value = await getSkills().catch(() => [])
})
</script>

<template>
  <section id="skills" class="art-section">
    <div class="art-container">
      <header class="head">
        <h2>技能</h2>
        <p class="meta">02 — Skills / Stack</p>
      </header>
      <hr class="rule" />

      <div class="grid">
        <article v-for="(g, i) in skills" :key="g.category" class="group">
          <p class="meta">{{ String(i + 1).padStart(2, '0') }}</p>
          <h3>{{ g.category }}</h3>
          <ul>
            <li v-for="item in g.items" :key="item.name">
              <div class="row">
                <span class="name">{{ item.name }}</span>
                <span class="lvl">{{ item.level }}</span>
              </div>
              <p>{{ item.desc }}</p>
            </li>
          </ul>
        </article>
      </div>
    </div>
  </section>
</template>

<style scoped>
.head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 20px;
}
h2 {
  margin: 0;
  font-size: clamp(48px, 7vw, 92px);
}
.grid {
  display: grid;
  gap: 0;
  padding-top: 12px;
}
.group {
  padding: 36px 0;
  border-bottom: 1px solid var(--line);
}
h3 {
  margin: 8px 0 20px;
  font-size: clamp(28px, 3vw, 40px);
}
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
li { padding: 12px 0; }
.row {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 6px;
}
.name { font-size: 15px; }
.lvl {
  font-size: 11px;
  letter-spacing: 0.16em;
  color: var(--vermilion);
}
li p {
  margin: 8px 0 0;
  font-size: 13px;
  color: var(--warm-gray);
}
@media (min-width: 800px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
    column-gap: 64px;
  }
  .group:nth-child(odd) { padding-right: 24px; }
}
</style>
