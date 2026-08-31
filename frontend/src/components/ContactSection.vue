<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { getProfile } from '../api'

const profile = ref({})

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})

async function copy(text, label) {
  try {
    await navigator.clipboard.writeText(text)
    ElMessage.success(`${label}已复制：${text}`)
  } catch {
    ElMessage.warning(`复制失败，请手动复制：${text}`)
  }
}
</script>

<template>
  <section id="contact" class="hd-section">
    <div class="hd-container">
      <div class="hd-section-title">
        <h2>找到我</h2>
        <svg class="squiggle" viewBox="0 0 120 20" fill="none">
          <path
            d="M4 12 C 20 4, 32 18, 48 11 C 64 4, 78 18, 94 11 C 104 7, 110 9, 116 10"
            stroke="#ff4d4d" stroke-width="3" stroke-linecap="round"
          />
        </svg>
      </div>

      <p class="invite">
        正在寻找数据分析相关机会，欢迎通过下面的方式联系我 ——
        点一下就能复制 📋
      </p>

      <div class="grid">
        <button class="hd-card contact-card" @click="copy(profile.phone, '手机号')">
          <span class="hd-tack"></span>
          <span class="icon-circle">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" />
            </svg>
          </span>
          <span class="label">电话</span>
          <span class="value">{{ profile.phone }}</span>
          <span class="hint">点击复制</span>
        </button>

        <button class="hd-card contact-card rev" @click="copy(profile.email, '邮箱')">
          <span class="hd-tack"></span>
          <span class="icon-circle blue">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="5" width="18" height="14" rx="2" />
              <path d="M3 7l9 6 9-6" />
            </svg>
          </span>
          <span class="label">邮箱</span>
          <span class="value">{{ profile.email }}</span>
          <span class="hint">点击复制</span>
        </button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.invite {
  font-size: 19px;
  margin: -16px 0 36px;
  color: rgba(45, 45, 45, 0.75);
}
.grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 32px;
  max-width: 640px;
  margin: 0 auto;
}
@media (min-width: 640px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
.contact-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 36px 24px 24px;
  font-family: var(--font-body);
  font-size: 17px;
  color: var(--hd-fg);
  cursor: pointer;
  text-align: center;
}
.contact-card.rev {
  transform: rotate(1deg);
}
.icon-circle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  margin-bottom: 8px;
  border: 2.5px solid var(--hd-border);
  border-radius: 50% 46% 54% 48% / 47% 53% 47% 53%;
  color: var(--hd-accent);
  background: #fff;
}
.icon-circle.blue {
  color: var(--hd-blue);
}
.icon-circle svg {
  width: 26px;
  height: 26px;
}
.label {
  font-family: var(--font-marker);
  font-size: 22px;
}
.value {
  font-size: 19px;
  font-weight: 700;
}
.hint {
  font-size: 14px;
  color: rgba(45, 45, 45, 0.45);
}
.contact-card:hover .value {
  text-decoration: underline wavy var(--hd-accent) 2px;
  text-underline-offset: 5px;
}
</style>
