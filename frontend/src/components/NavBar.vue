<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})
const menuOpen = ref(false)
const links = [
  { id: 'home', label: '首页' },
  { id: 'about', label: '关于我' },
  { id: 'skills', label: '技能' },
  { id: 'projects', label: '项目' },
  { id: 'education', label: '教育' },
  { id: 'contact', label: '联系' },
]

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})

function go(id) {
  menuOpen.value = false
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <header class="nav-wrap">
    <div class="nav hd-container">
      <a class="logo" href="#home" @click.prevent="go('home')">
        <span class="logo-sticker">{{ profile.name || '陆杨磊' }}</span>
      </a>

      <nav class="links">
        <a
          v-for="l in links"
          :key="l.id"
          class="hd-link"
          :href="'#' + l.id"
          @click.prevent="go(l.id)"
        >
          {{ l.label }}
        </a>
      </nav>

      <button class="burger" aria-label="菜单" @click="menuOpen = !menuOpen">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round">
          <path d="M4 7 C10 6.4, 16 7.6, 21 7" />
          <path d="M3 12 C9 12.7, 15 11.5, 21 12" />
          <path d="M4 17 C11 16.4, 16 17.5, 20 17" />
        </svg>
      </button>
    </div>

    <transition name="drop">
      <nav v-if="menuOpen" class="mobile-menu">
        <a
          v-for="l in links"
          :key="l.id"
          href="#"
          @click.prevent="go(l.id)"
        >
          {{ l.label }}
        </a>
      </nav>
    </transition>
  </header>
</template>

<style scoped>
.nav-wrap {
  position: sticky;
  top: 12px;
  z-index: 100;
  padding: 0 16px;
}
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  background: #fff;
  border: 3px solid var(--hd-border);
  border-radius: var(--wobbly);
  box-shadow: var(--shadow);
  padding: 8px 24px;
  transform: rotate(-0.4deg);
}
.logo {
  text-decoration: none;
  color: inherit;
}
.logo-sticker {
  display: inline-block;
  font-family: var(--font-marker);
  font-size: 22px;
  background: var(--hd-postit);
  border: 2px solid var(--hd-border);
  border-radius: var(--wobbly-sm);
  padding: 0 14px;
  transform: rotate(-2deg);
}
.links {
  display: flex;
  gap: 22px;
  font-size: 18px;
}
.links a {
  color: inherit;
  text-decoration: none;
}
.links a:hover {
  color: var(--hd-accent);
  text-decoration: underline wavy var(--hd-accent) 2px;
  text-underline-offset: 5px;
}
.burger {
  display: none;
  background: none;
  border: none;
  color: var(--hd-fg);
  cursor: pointer;
  padding: 4px;
}
.mobile-menu {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
  background: #fff;
  border: 3px solid var(--hd-border);
  border-radius: var(--wobbly-md);
  box-shadow: var(--shadow);
  padding: 12px 24px;
  transform: rotate(-0.4deg);
}
.mobile-menu a {
  color: inherit;
  text-decoration: none;
  font-size: 19px;
  padding: 8px 0;
  border-bottom: 2px dashed var(--hd-muted);
}
.mobile-menu a:last-child {
  border-bottom: none;
}
.drop-enter-active,
.drop-leave-active {
  transition: all 0.15s ease;
}
.drop-enter-from,
.drop-leave-to {
  opacity: 0;
  transform: translateY(-8px) rotate(-0.4deg);
}
@media (max-width: 768px) {
  .links { display: none; }
  .burger { display: block; }
}
</style>
