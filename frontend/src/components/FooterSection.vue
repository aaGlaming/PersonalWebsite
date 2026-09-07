<script setup>
import { ref, onMounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})
const year = new Date().getFullYear()

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})

function top() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<template>
  <footer class="footer">
    <div class="art-container">
      <hr class="rule" />
      <div class="inner">
        <p class="sig">
          {{ profile.name }}
          <span>{{ profile.title }}</span>
        </p>
        <nav>
          <a :href="`mailto:${profile.email}`">Write</a>
          <a href="#home" @click.prevent="top">Index ↑</a>
        </nav>
        <p class="copy">© {{ year }} {{ profile.studio || 'Atelier' }} · Ivory / Charcoal / Vermilion</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  padding: 0 0 48px;
}
.inner {
  display: grid;
  gap: 16px;
  padding-top: 28px;
}
.sig {
  margin: 0;
  font-family: var(--font-serif);
  font-size: 28px;
}
.sig span {
  display: block;
  font-family: var(--font-sans);
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--warm-gray);
  margin-top: 6px;
}
nav {
  display: flex;
  gap: 24px;
}
nav a {
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  text-decoration: none;
  border-bottom: 1px solid transparent;
}
nav a:hover { border-bottom-color: var(--vermilion); color: var(--vermilion); }
.copy {
  margin: 0;
  font-size: 11px;
  letter-spacing: 0.08em;
  color: var(--warm-gray);
}
@media (min-width: 720px) {
  .inner {
    grid-template-columns: 1fr auto auto;
    align-items: end;
  }
}
</style>
