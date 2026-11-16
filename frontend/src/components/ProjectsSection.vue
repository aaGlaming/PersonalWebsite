<script setup>
import { computed, onMounted, ref } from 'vue'
import { getProjects } from '../api'
import ProjectCard from './ProjectCard.vue'

const projects = ref([])
const status = ref('loading')
const resumeProjects = computed(() => projects.value.filter(p => p.category === 'resume'))
const practiceProjects = computed(() => projects.value.filter(p => p.category !== 'resume'))
async function loadProjects() {
  status.value = 'loading'
  try {
    projects.value = await getProjects()
    status.value = 'ready'
  } catch {
    status.value = 'error'
  }
}
onMounted(loadProjects)
</script>

<template>
  <section id="projects" class="art-section">
    <div class="art-container">
      <header class="head">
        <p class="meta">03 — Selected projects</p>
        <h2>项目</h2>
      </header>
      <p class="lede">两段团队项目经历：从业务输入到 Agent 执行，再到结果核验。这里记录我的模块开发与流程衔接工作。</p>
      <hr class="rule" />
      <p v-if="status === 'loading'" role="status">正在加载项目…</p>
      <p v-else-if="status === 'error'" role="alert">
        项目暂时未能加载。<button type="button" @click="loadProjects">重新加载</button>
      </p>
      <template v-else>
        <nav class="index" aria-label="项目目录">
          <a v-for="(project, i) in resumeProjects" :key="project.id" :href="'#' + project.id">
            <span>0{{ i + 1 }}</span> {{ project.name }} ↗
          </a>
        </nav>
        <ProjectCard v-for="(project, i) in resumeProjects" :key="project.id" :project="project" :index="i + 1" />
        <header v-if="practiceProjects.length" class="practice">
          <p class="meta">Personal explorations</p>
          <h3>更多实践</h3>
          <p>个人知识库与 Web 作品。</p>
        </header>
        <ProjectCard v-for="(project, i) in practiceProjects" :key="project.id" :project="project" :index="i + 3" compact />
      </template>
    </div>
  </section>
</template>

<style scoped>
.head { display:flex; align-items:baseline; justify-content:space-between; gap:16px; margin-bottom:12px; }
h2 { margin:0; font-size:clamp(48px,7vw,92px); }
.lede { max-width:64ch; color:var(--warm-gray); font-size:15px; margin:0 0 28px; }
.index { display:flex; flex-wrap:wrap; gap:16px 32px; padding:24px 0; border-bottom:1px solid var(--line); }
.index a { color:var(--charcoal); font-size:14px; text-decoration:none; }
.index span { color:var(--vermilion); margin-right:8px; }
.index a:hover { color:var(--vermilion); }
.practice { margin-top:72px; }
.practice h3 { font-size:36px; margin:12px 0; }
.practice p:last-child { color:var(--warm-gray); }
button { font:inherit; color:var(--vermilion); cursor:pointer; }
</style>
