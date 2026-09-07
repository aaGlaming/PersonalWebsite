<script setup>
import { ref, onMounted } from 'vue'
import { getProfile } from '../api'

const profile = ref({})

onMounted(async () => {
  profile.value = await getProfile().catch(() => ({}))
})

function go(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <section id="home" class="hero">
    <div class="art-container frame">
      <div class="col copy">
        <p class="meta kicker">
          {{ profile.studio || 'ATELIER L.Y.L.' }}
          <span>·</span>
          {{ profile.location || 'Chongqing' }}
          <span>·</span>
          Ed. 2026
        </p>
        <h1>
          <span>Work</span>
          <span>is a</span>
          <span class="accent">record.</span>
        </h1>
        <p class="lead">
          {{ profile.name }}
          <em>{{ profile.title }}</em>
        </p>
        <p class="slogan">{{ profile.slogan }}</p>
        <div class="actions">
          <a class="art-link" href="#projects" @click.prevent="go('projects')">
            View works <span class="arrow">→</span>
          </a>
          <a class="art-link" href="#contact" @click.prevent="go('contact')">
            Contact
          </a>
        </div>
      </div>

      <aside class="col plate" aria-hidden="true">
        <div class="plate-inner">
          <p class="vert">Exhibition / 01</p>
          <div class="block"></div>
          <p class="caption">
            FIG. 00
            <br />Untitled Portrait
            <br />Charcoal on ivory
            <br />{{ profile.name }}
          </p>
        </div>
      </aside>
    </div>
    <p class="foot-meta art-container">
      {{ profile.phone }}
      <span>/</span>
      {{ profile.email }}
    </p>
  </section>
</template>

<style scoped>
.hero {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 88px 0 48px;
}
.frame {
  display: grid;
  gap: 48px;
  align-items: end;
}
.kicker {
  margin: 0 0 28px;
}
.kicker span { margin: 0 8px; color: var(--vermilion); }
h1 {
  margin: 0;
  font-size: clamp(64px, 9vw, 160px);
  display: flex;
  flex-direction: column;
}
h1 span { display: block; }
.accent { color: var(--vermilion); font-style: italic; }
.lead {
  margin: 28px 0 0;
  font-size: 18px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.lead em {
  font-style: normal;
  color: var(--warm-gray);
  font-size: 13px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}
.slogan {
  max-width: 28ch;
  margin: 20px 0 0;
  color: color-mix(in srgb, var(--charcoal) 72%, transparent);
}
.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 28px;
  margin-top: 36px;
}
.plate {
  min-height: 320px;
}
.plate-inner {
  position: relative;
  height: 100%;
  min-height: 360px;
  background: var(--charcoal);
  color: var(--paper);
  padding: 24px;
  display: grid;
  grid-template-rows: auto 1fr auto;
}
.vert {
  margin: 0;
  writing-mode: vertical-rl;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  font-size: 10px;
  color: color-mix(in srgb, var(--paper) 55%, transparent);
  justify-self: end;
}
.block {
  width: min(46%, 180px);
  height: 42%;
  background: var(--vermilion);
  justify-self: start;
  align-self: center;
  margin-left: 8%;
}
.caption {
  margin: 0;
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  line-height: 1.7;
  color: color-mix(in srgb, var(--paper) 70%, transparent);
}
.foot-meta {
  margin-top: 48px;
  font-size: 11px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--warm-gray);
}
.foot-meta span { margin: 0 12px; color: var(--vermilion); }
@media (min-width: 900px) {
  .frame {
    grid-template-columns: 7fr 5fr;
    gap: 64px;
  }
  .plate-inner { min-height: 520px; }
}
</style>
