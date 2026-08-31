<script setup>
import { ref, onMounted } from 'vue'
import { getSkills } from '../api'

const skills = ref([])

onMounted(async () => {
  skills.value = await getSkills().catch(() => [])
})
</script>

<template>
  <section id="skills" class="hd-section">
    <div class="hd-container">
      <div class="hd-section-title">
        <svg class="squiggle" viewBox="0 0 120 20" fill="none">
          <path
            d="M4 10 C 20 16, 32 4, 48 10 C 64 16, 78 4, 94 10 C 104 13, 110 11, 116 10"
            stroke="#2d5da1" stroke-width="3" stroke-linecap="round"
          />
        </svg>
        <h2>技能点</h2>
      </div>

      <div class="grid">
        <div
          v-for="(g, i) in skills"
          :key="g.category"
          class="hd-card group"
          :style="{ transform: `rotate(${[0.8, -1, 1, -0.8][i % 4]}deg)` }"
        >
          <h3 class="group-title">
            <span class="icon-circle">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
                <template v-if="g.icon === 'code'">
                  <path d="M8 7 3 12l5 5" /><path d="M16 7l5 5-5 5" />
                </template>
                <template v-else-if="g.icon === 'brain'">
                  <circle cx="12" cy="12" r="8.5" />
                  <path d="M8.5 11 C10 9, 13 9, 14 11 C15 13.5, 12 15.5, 10 14.5" />
                </template>
                <template v-else-if="g.icon === 'database'">
                  <ellipse cx="12" cy="5.5" rx="7.5" ry="3" />
                  <path d="M4.5 5.5v6.5c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3V5.5" />
                  <path d="M4.5 12v6c0 1.7 3.4 3 7.5 3s7.5-1.3 7.5-3v-6" />
                </template>
                <template v-else>
                  <path d="M4 20V9" /><path d="M10 20V4" /><path d="M16 20v-8" /><path d="M22 20H2" />
                </template>
              </svg>
            </span>
            {{ g.category }}
          </h3>

          <div v-for="item in g.items" :key="item.name" class="skill">
            <div class="skill-head">
              <span class="skill-name">{{ item.name }}</span>
              <span class="skill-desc">{{ item.desc }}</span>
            </div>
            <div class="hd-bar">
              <div class="hd-bar-fill" :style="{ width: item.level + '%' }"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 28px;
}
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
.group {
  padding: 26px 26px 20px;
  transition: transform 0.1s ease;
}
.group:hover {
  transform: rotate(0deg) !important;
}
.group-title {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 0 0 18px;
  font-size: 24px;
}
.icon-circle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border: 2.5px solid var(--hd-border);
  border-radius: 52% 48% 46% 54% / 48% 54% 46% 52%;
  color: var(--hd-accent);
  background: #fff;
}
.icon-circle svg {
  width: 22px;
  height: 22px;
}
.skill {
  margin-bottom: 16px;
}
.skill-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 10px;
  margin-bottom: 5px;
}
.skill-name {
  font-size: 18px;
  font-weight: 700;
  white-space: nowrap;
}
.skill-desc {
  font-size: 14px;
  color: rgba(45, 45, 45, 0.55);
  text-align: right;
}
</style>
