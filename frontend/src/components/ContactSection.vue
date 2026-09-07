<script setup>
import { ref, onMounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})
const toast = ref('')
let timer = 0

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})

async function copy(text, label) {
  if (!text) return
  try {
    await navigator.clipboard.writeText(text)
    toast.value = `${label} copied`
  } catch {
    toast.value = `请手动复制 ${text}`
  }
  clearTimeout(timer)
  timer = window.setTimeout(() => { toast.value = '' }, 2200)
}
</script>

<template>
  <section id="contact" class="art-section">
    <div class="art-container">
      <header class="head">
        <p class="meta">05 — Correspondence</p>
        <h2>联系</h2>
      </header>
      <p class="invite">正在寻找 AI 应用开发相关机会。点击条目即可复制。</p>
      <hr class="rule" />

      <div class="rows">
        <button type="button" @click="copy(profile.phone, 'Phone')">
          <span class="k">Telephone</span>
          <span class="v">{{ profile.phone }}</span>
          <span class="h">Copy →</span>
        </button>
        <button type="button" @click="copy(profile.email, 'Email')">
          <span class="k">Email</span>
          <span class="v">{{ profile.email }}</span>
          <span class="h">Copy →</span>
        </button>
      </div>
    </div>
    <p v-if="toast" class="toast" role="status">{{ toast }}</p>
  </section>
</template>

<style scoped>
.head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 12px;
}
h2 {
  margin: 0;
  font-size: clamp(48px, 7vw, 92px);
}
.invite {
  margin: 0 0 28px;
  color: var(--warm-gray);
}
.rows {
  display: grid;
  padding-top: 8px;
}
button {
  display: grid;
  grid-template-columns: 120px 1fr auto;
  gap: 16px;
  align-items: baseline;
  width: 100%;
  padding: 28px 0;
  border: 0;
  border-bottom: 1px solid var(--line-strong);
  background: none;
  color: inherit;
  font: inherit;
  text-align: left;
  cursor: pointer;
}
button:first-child { border-top: 1px solid var(--line-strong); }
.k {
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--warm-gray);
}
.v {
  font-family: var(--font-serif);
  font-size: clamp(22px, 3vw, 36px);
}
.h {
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--vermilion);
  opacity: 0;
  transition: opacity 0.3s ease;
}
button:hover .h,
button:focus-visible .h {
  opacity: 1;
}
@media (max-width: 640px) {
  button {
    grid-template-columns: 1fr;
    gap: 6px;
  }
  .h { opacity: 1; }
}
</style>
