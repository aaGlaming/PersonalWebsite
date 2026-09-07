<script setup>
import { ref, onMounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})
</script>

<template>
  <section id="about" class="art-section">
    <div class="art-container">
      <header class="head">
        <p class="meta">01 — Biography</p>
        <h2>关于</h2>
      </header>
      <hr class="rule" />

      <div class="layout">
        <p class="intro">
          <span class="drop">{{ (profile.intro || '重').slice(0, 1) }}</span>
          {{ (profile.intro || '').slice(1) }}
        </p>

        <ol class="notes">
          <li v-for="(h, i) in profile.highlights || []" :key="h.title">
            <span class="idx">Fig. {{ String(i + 1).padStart(2, '0') }}</span>
            <h3>{{ h.title }}</h3>
            <p>{{ h.body }}</p>
          </li>
        </ol>
      </div>
    </div>
  </section>
</template>

<style scoped>
.head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 20px;
}
h2 {
  margin: 0;
  font-size: clamp(48px, 7vw, 92px);
}
.layout {
  display: grid;
  gap: 56px;
  padding-top: 48px;
}
.intro {
  margin: 0;
  font-size: clamp(18px, 2vw, 22px);
  line-height: 1.75;
  max-width: 46ch;
}
.drop {
  float: left;
  font-family: var(--font-serif);
  font-size: 86px;
  line-height: 0.75;
  padding: 8px 12px 0 0;
  color: var(--vermilion);
}
.notes {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0;
}
.notes li {
  padding: 22px 0;
  border-top: 1px solid var(--line);
}
.notes li:last-child { border-bottom: 1px solid var(--line); }
.idx {
  display: block;
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--vermilion);
  margin-bottom: 8px;
}
h3 {
  margin: 0 0 8px;
  font-size: 28px;
}
.notes p {
  margin: 0;
  color: color-mix(in srgb, var(--charcoal) 75%, transparent);
  font-size: 15px;
}
@media (min-width: 900px) {
  .layout {
    grid-template-columns: 7fr 5fr;
    align-items: start;
  }
}
</style>
