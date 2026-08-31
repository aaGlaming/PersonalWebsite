import axios from 'axios'

// 相对路径 data/*.json：Flask 模式由 /api/data/<name>.json 提供，
// 静态托管模式（EdgeOne Pages 等）由 public/data/ 下的同名文件提供
const http = axios.create({ baseURL: 'data', timeout: 10000 })

export const getProfile = () => http.get('/profile.json').then((r) => r.data)
export const getSkills = () => http.get('/skills.json').then((r) => r.data)
export const getProjects = () => http.get('/projects.json').then((r) => r.data)
export const getEducation = () => http.get('/education.json').then((r) => r.data)
