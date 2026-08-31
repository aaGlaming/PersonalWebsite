<script setup>
import { ref, onMounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})
</script>

<template>
  <section id="about" class="hd-section">
    <div class="hd-container">
      <div class="hd-section-title">
        <h2>关于我</h2>
        <svg class="squiggle" viewBox="0 0 120 20" fill="none">
          <path
            d="M4 12 C 20 4, 32 18, 48 11 C 64 4, 78 18, 94 11 C 104 7, 110 9, 116 10"
            stroke="#ff4d4d" stroke-width="3" stroke-linecap="round"
          />
        </svg>
      </div>

      <div class="hd-card intro-card">
        <span class="hd-tape"></span>
        <p>
          <span class="dropcap">{{ (profile.intro || '').slice(0, 1) }}</span>
          {{ (profile.intro || '').slice(1) }}
        </p>
      </div>

      <div class="grid">
        <div
          v-for="(h, i) in profile.highlights || []"
          :key="h.title"
          class="hd-postit note"
          :style="{
            transform: `rotate(${[-1.6, 1.2, -1, 1.8][i % 4]}deg)`,
            marginTop: i % 2 ? '22px' : '0',
          }"
        >
          <span class="hd-tack"></span>
          <h3>{{ h.title }}</h3>
          <p>{{ h.body }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.intro-card {
  padding: 32px 36px;
  font-size: 19px;
  margin-bottom: 48px;
  transform: rotate(-0.3deg);
}
.dropcap {
  float: left;
  font-family: var(--font-marker);
  font-size: 56px;
  line-height: 1;
  padding: 4px 12px 0 0;
  color: var(--hd-accent);
}
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 28px;
}
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
.note {
  padding: 30px 26px 24px;
}
.note h3 {
  margin: 0 0 8px;
  font-size: 22px;
  color: var(--hd-blue);
}
.note p {
  margin: 0;
  font-size: 16px;
  line-height: 1.75;
}
</style>
