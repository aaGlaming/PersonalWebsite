<script setup>
import { ref, onMounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})
const year = new Date().getFullYear()

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})
</script>

<template>
  <footer class="footer">
    <svg class="wavy-top" viewBox="0 0 1200 30" preserveAspectRatio="none" fill="none">
      <path
        d="M0 15 C 100 2, 200 28, 300 15 C 400 2, 500 28, 600 15 C 700 2, 800 28, 900 15 C 1000 2, 1100 28, 1200 15"
        stroke="#2d2d2d" stroke-width="3" stroke-linecap="round" stroke-dasharray="10 8"
      />
    </svg>

    <div class="inner hd-container">
      <p class="sig">{{ profile.name }} · {{ profile.title }}</p>
      <nav class="flinks">
        <a :href="`mailto:${profile.email}`" class="hd-link">发邮件给我</a>
        <span class="dot">✦</span>
        <a href="#" class="hd-link" @click.prevent>回到顶部 ↑</a>
      </nav>
      <p class="copy">© {{ year }} 手写于纸上 · 用心排版于代码里</p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  margin-top: 40px;
  padding: 0 16px 32px;
}
.wavy-top {
  display: block;
  width: 100%;
  height: 30px;
}
.inner {
  text-align: center;
  padding-top: 24px;
}
.sig {
  font-family: var(--font-marker);
  font-size: 24px;
  margin: 0 0 10px;
}
.flinks {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 14px;
  font-size: 17px;
}
.dot {
  color: var(--hd-accent);
}
.copy {
  margin: 14px 0 0;
  font-size: 15px;
  color: rgba(45, 45, 45, 0.45);
}
</style>
