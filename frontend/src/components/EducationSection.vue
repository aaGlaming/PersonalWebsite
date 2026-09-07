<script setup>
import { ref, onMounted } from 'vue'
import { getEducation } from '../api'

const edu = ref({})

onMounted(async () => {
  edu.value = await getEducation().catch(() => ({}))
})
</script>

<template>
  <section id="education" class="art-section">
    <div class="art-container">
      <header class="head">
        <h2>档案</h2>
        <p class="meta">04 — Education / Honors</p>
      </header>
      <hr class="rule" />

      <div class="grid">
        <div class="school">
          <p class="meta">Collection</p>
          <h3>{{ edu.school }}</h3>
          <p class="degree">{{ edu.degree }}</p>
          <p class="period">{{ edu.period }}</p>
          <p class="note">{{ edu.note }}</p>
        </div>

        <ul class="honors">
          <li v-for="h in edu.honors || []" :key="h.name">
            <span class="time">{{ h.time }}</span>
            <span class="name">{{ h.name }}</span>
          </li>
        </ul>
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
  gap: 48px;
  padding-top: 48px;
}
.school h3 {
  margin: 12px 0 8px;
  font-size: clamp(36px, 5vw, 64px);
}
.degree {
  margin: 0;
  font-size: 16px;
}
.period {
  margin: 8px 0 20px;
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--vermilion);
}
.note {
  margin: 0;
  max-width: 40ch;
  color: var(--warm-gray);
}
.honors {
  list-style: none;
  margin: 0;
  padding: 0;
}
.honors li {
  display: grid;
  grid-template-columns: 88px 1fr;
  gap: 16px;
  padding: 18px 0;
  border-top: 1px solid var(--line);
  font-size: 16px;
}
.honors li:last-child { border-bottom: 1px solid var(--line); }
.time {
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--warm-gray);
  padding-top: 4px;
}
@media (min-width: 800px) {
  .grid { grid-template-columns: 1.1fr 0.9fr; }
}
</style>
