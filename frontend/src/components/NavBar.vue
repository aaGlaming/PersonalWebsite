<script setup>
import { ref, onMounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})
const menuOpen = ref(false)
const links = [
  { id: 'home', no: '00', label: 'Index' },
  { id: 'about', no: '01', label: 'About' },
  { id: 'skills', no: '02', label: 'Skills' },
  { id: 'projects', no: '03', label: 'Works' },
  { id: 'education', no: '04', label: 'Archive' },
  { id: 'contact', no: '05', label: 'Contact' },
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
    <div class="nav art-container">
      <a class="logo" href="#home" @click.prevent="go('home')">
        <span class="logo-k">{{ profile.studio || 'ATELIER' }}</span>
        <span class="logo-n">{{ profile.name || '陆杨磊' }}</span>
      </a>

      <nav class="links" aria-label="站点导航">
        <a
          v-for="l in links"
          :key="l.id"
          :href="'#' + l.id"
          @click.prevent="go(l.id)"
        >
          <span class="no">{{ l.no }}</span>
          {{ l.label }}
        </a>
      </nav>

      <span class="year">2026</span>

      <button
        class="burger"
        type="button"
        :aria-expanded="menuOpen"
        aria-label="打开菜单"
        @click="menuOpen = !menuOpen"
      >
        {{ menuOpen ? 'Close' : 'Menu' }}
      </button>
    </div>

    <nav v-if="menuOpen" class="mobile" aria-label="移动导航">
      <a
        v-for="l in links"
        :key="l.id"
        :href="'#' + l.id"
        @click.prevent="go(l.id)"
      >
        <span>{{ l.no }}</span>
        {{ l.label }}
      </a>
    </nav>
  </header>
</template>

<style scoped>
.nav-wrap {
  position: sticky;
  top: 0;
  z-index: 100;
  background: color-mix(in srgb, var(--paper) 88%, transparent);
  backdrop-filter: none;
  border-bottom: 1px solid var(--line);
}
.nav {
  display: grid;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: 24px;
  min-height: 64px;
}
.logo {
  display: flex;
  flex-direction: column;
  gap: 2px;
  text-decoration: none;
}
.logo-k {
  font-size: 10px;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--warm-gray);
}
.logo-n {
  font-family: var(--font-serif);
  font-size: 18px;
  letter-spacing: 0.04em;
}
.links {
  display: none;
  gap: 22px;
}
.links a {
  display: inline-flex;
  align-items: baseline;
  gap: 6px;
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--charcoal);
}
.links a:hover .no,
.links a:focus-visible .no {
  color: var(--vermilion);
}
.no {
  font-size: 9px;
  color: var(--warm-gray);
}
.year {
  font-size: 11px;
  letter-spacing: 0.2em;
  color: var(--warm-gray);
}
.burger {
  display: block;
  background: none;
  border: 0;
  padding: 0;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--charcoal);
  cursor: pointer;
}
.mobile {
  display: flex;
  flex-direction: column;
  padding: 8px var(--pad) 24px;
  border-top: 1px solid var(--line);
}
.mobile a {
  display: flex;
  gap: 16px;
  padding: 14px 0;
  border-bottom: 1px solid var(--line);
  text-decoration: none;
  font-family: var(--font-serif);
  font-size: 32px;
}
.mobile a span {
  font-family: var(--font-sans);
  font-size: 11px;
  letter-spacing: 0.16em;
  color: var(--vermilion);
  padding-top: 14px;
}
@media (min-width: 960px) {
  .links { display: flex; }
  .burger, .mobile { display: none; }
}
</style>
