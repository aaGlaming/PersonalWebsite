<script setup>
import { ref, onMounted } from 'vue'
import { getEducation } from '../api'

const edu = ref({})

onMounted(async () => {
  edu.value = await getEducation().catch(() => ({}))
})
</script>

<template>
  <section id="education" class="hd-section">
    <div class="hd-container">
      <div class="hd-section-title">
        <svg class="squiggle" viewBox="0 0 120 20" fill="none">
          <path
            d="M4 10 C 20 16, 32 4, 48 10 C 64 16, 78 4, 94 10 C 104 13, 110 11, 116 10"
            stroke="#2d5da1" stroke-width="3" stroke-linecap="round"
          />
        </svg>
        <h2>教育与荣誉</h2>
      </div>

      <div class="grid">
        <div class="hd-card edu-card">
          <span class="hd-tape"></span>
          <div class="cap">🎓</div>
          <h3>{{ edu.school }}</h3>
          <p class="degree">{{ edu.degree }}</p>
          <p class="period">{{ edu.period }}</p>
          <p class="note">{{ edu.note }}</p>
        </div>

        <div class="honors">
          <span class="hd-sticker honors-label">荣誉奖项 ✦</span>
          <el-timeline>
            <el-timeline-item
              v-for="h in edu.honors || []"
              :key="h.name"
              :timestamp="h.time"
              placement="top"
            >
              <div class="hd-card honor-card">{{ h.name }}</div>
            </el-timeline-item>
          </el-timeline>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 40px;
  align-items: start;
}
@media (min-width: 768px) {
  .grid { grid-template-columns: 1fr 1fr; }
}
.edu-card {
  padding: 34px 30px 26px;
  transform: rotate(-0.8deg);
}
.cap {
  font-size: 40px;
  margin-bottom: 6px;
}
.edu-card h3 {
  margin: 0 0 4px;
  font-size: 28px;
}
.degree {
  margin: 0 0 2px;
  font-size: 18px;
  font-weight: 700;
  color: var(--hd-blue);
}
.period {
  margin: 0 0 10px;
  font-family: var(--font-hand);
  color: rgba(45, 45, 45, 0.55);
}
.note {
  margin: 0;
  font-size: 16px;
  border-top: 2px dashed var(--hd-muted);
  padding-top: 12px;
}
.honors {
  position: relative;
  padding-top: 46px;
}
.honors-label {
  position: absolute;
  top: 0;
  left: -6px;
  z-index: 2;
  font-size: 17px;
}
.honor-card {
  padding: 14px 20px;
  font-size: 17px;
  font-weight: 700;
}
</style>
