import express from 'express'
let router = express.Router()

import list from './routes/list'
import show from './routes/show'
import search from './routes/search'
import filter from './routes/filter'

import validation from '../validation'

router.get('/',
  validation.limit,
  validation.skip,
  validation.sort,
  list)

router.get('/search',
  validation.query,
  validation.limit,
  validation.skip,
  validation.sort,
  search)

router.get('/filter',
  validation.query,
  validation.filterQuery,
  validation.limit,
  validation.skip,
  validation.sort,
  filter)

router.get('/:id',
  validation.id,
  show)

export default router
