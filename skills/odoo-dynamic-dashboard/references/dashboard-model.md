# Dashboard models, fields, and values

Verified against `dynamic_dashboard_ai_nexgen` 20.0.1.0.15 source. Use these exact
technical values; the validator rejects anything else.

## `dynamic.dashboard` (the board)

| Field | Notes |
|---|---|
| `name` | Required, translatable. |
| `category` | Char; a matching `dynamic.dashboard.category` is created automatically. |
| `group_ids` | Groups that may open the board; default internal users. |
| `chart_theme` | `default, cool, warm, neon, pastel, corporate, vibrant, ocean, sunset`; overrides item themes when set. |
| `default_date_filter` | Default period for the board: `none, today, this_week, this_month, this_quarter, this_year, last_7_days, last_30_days, last_90_days, last_month, last_quarter, last_year, year_to_date, month_to_date`, and the other values listed for items. |
| `background_color` | Hex, e.g. `#F7F8FA`. |
| `sequence`, `company_id` | Usual meaning. |

## `dynamic.dashboard.item` (tile or chart)

### Type and size

`item_type` and its recommended `grid_w` x `grid_h` on the 12-column grid:

| Size | Types |
|---|---|
| 3 x 2 | `tile`, `kpi` |
| 3 x 3 | `gauge`, `radialBar` |
| 6 x 3 | `scorecard`, `bullet` |
| 4 x 4 | `pie`, `doughnut`, `polarArea`, `radar`, `flower`, `venn`, `pictorial`, `spiral` |
| 6 x 4 | `bar`, `barLine`, `horizontalBar`, `line`, `area`, `stepLine`, `smoothedLine`, `waterfall`, `scatter`, `candlestick`, `ohlc`, `wordCloud`, `todo` |
| 4 x 5 | `funnel`, `pyramid` |
| 6 x 5 | `treemap`, `sunburst`, `forceDirected`, `pack`, `tree`, `partition`, `voronoiTreemap`, `chord`, `chordDirected`, `chordNonRibbon`, `map`, `mapPoints`, `heatmap`, `matrixHeatmap`, `list`, `iframe` |
| 12 x 4 | `arcDiagram`, `timeline`, `serpentine` |
| 12 x 5 | `sankey` |
| 12 x 6 | `odoo_view` |

Grid rules: `grid_x >= 0`, `grid_y >= 0`, `grid_w` 1 to 12 with `grid_x + grid_w <= 12`,
`grid_h >= 1`, no two items overlapping on one dashboard.

### Data source

| Field | Notes |
|---|---|
| `dashboard_id` | Required. |
| `data_calculation_type` | `custom` (Odoo model, default), `sql`. Other values (`api, excel, csv, scrape, sheets`) need connections or files and are out of scope. |
| `model_id` | `ir.model`; required for `custom`. |
| `domain` | Python list literal as text, e.g. `[('state', '=', 'posted')]`. |
| `data_type` | `sum`, `count`, `average`. `sum`/`average` need `measure_field_ids`. |
| `measure_field_ids` | Stored integer, float, or monetary fields; first one is the main value. |
| `measure_field_2_ids` | Second measure set (e.g. bar + line). |
| `group_by_field_id`, `sub_group_by_field_id` | Stored fields; for date fields set `group_by_date_type`. |
| `group_by_date_type`, `sub_group_by_date_type` | `minute, hour, day, week, month, quarter, year`. |
| `sort_by_field_id`, `sort_order` (`asc`, `desc`), `record_limit` | Top-N charts. `record_limit` silently drops the remaining groups: for "per hub" or "per partner" charts that must show every group, set it above the expected group count. |
| `list_view_field_ids` | Columns for `list` items. |
| `date_filter_field_id` | Stored date or datetime field the period applies to. |
| `date_filter_selection` | `none, today, yesterday, tomorrow, this_week, this_month, this_quarter, this_year, next_week, next_month, next_quarter, next_year, week_to_date, month_to_date, year_to_date, last_7_days, last_30_days, last_90_days, last_week, last_month, last_quarter, last_year, past_until_now, future_starting_now, custom, user_defined`. `custom` needs `item_start_date` and `item_end_date`. |
| `compare_previous_period` | Boolean; tiles show the change vs the previous period. |
| `kpi_id` | Show a `dynamic.dashboard.kpi`; the KPI then drives the value. |
| `query` | SQL items only; see `sql-items.md`. |
| `allowed_group_ids` | Restrict who sees this item. Required for SQL items. |

Analytic data: from Odoo 17, `account.analytic.line.account_id` holds only the first
analytic plan; other plans live in database-specific columns (`x_plan<N>_id`). Do not
group or filter on them in reusable XML; group the source records by their own field
(for example a stored `hub_id` on the document line) instead.

### Presentation

| Field | Values |
|---|---|
| `tile_icon` | `fa-bar-chart, fa-line-chart, fa-area-chart, fa-pie-chart, fa-dashboard, fa-tachometer, fa-money, fa-usd, fa-eur, fa-shopping-cart, fa-credit-card, fa-truck, fa-archive, fa-calculator, fa-users, fa-user, fa-building, fa-briefcase, fa-database, fa-flask, fa-list, fa-check, fa-star, fa-heart, fa-globe, fa-calendar, fa-clock-o, fa-envelope, fa-phone, fa-tag, fa-tags, fa-cubes, fa-cube, fa-percent, fa-signal, fa-trophy, fa-bolt, fa-fire, fa-leaf, fa-home` (default `fa-bar-chart`) |
| `tile_layout` | `layout1` to `layout8` |
| `tile_theme` | `custom, ocean, sky, indigo, violet, plum, berry, rose, coral, tangerine, amber, sunflower, forest, emerald, mint, teal, slate, graphite, navy, midnight` |
| `unit` | `$, €, £, ¥, %, kg, g, lb, m, cm, km, hrs, days, pcs, u, units` (leave empty for local currency amounts) |
| `enable_target`, `standard_target_value`, `target_view` (`number`, `progress_bar`) | Targets on tiles; period targets are `dynamic.dashboard.target.line` records (`item_id`, `date_start`, `date_end`, `target_value`). Use these for amounts against a target. |

Segment colours: `dynamic.dashboard.item.color` with `item_id`, `segment_name`
(exact label), `color` (hex), unique per item and label.

## `dynamic.dashboard.kpi`

| Field | Notes |
|---|---|
| `name` | Required; formulas refer to children by name in braces. |
| `parent_id` | Builds the tree. |
| `computation_mode` | `model` (needs `model_id`), `formula` (needs `formula`, e.g. `{Won}-{Lost}`), `children` (sum of children). With addon 20.0.1.0.15 on Odoo 20, `model` works only with aggregation `count`; see `odoo-20-community.md`. |
| `aggregation` | `sum`, `count`, `average`. |
| `domain`, `date_filter_field_id` | As for items. |
| `target_ids` | `dynamic.dashboard.kpi.target` lines with a period and value. |

## `dynamic.dashboard.filter` (global filter)

`dashboard_id`, `name`, `model_id`, `domain` (required), `widget_type`
(`toggle`, `selection`, `many2one`, `date`; the last three need `filter_field_id`),
`is_linked`, `is_active`.
