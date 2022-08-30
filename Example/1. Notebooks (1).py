# Databricks notebook source
# MAGIC %md
# MAGIC * Collection of runnable cells (commands)
# MAGIC * Mix programming languages by using %< language > at the beginning of a cell
# MAGIC * Run a notebook from another notebook by using the %run < notebook > magic command
# MAGIC * All variables defined in < notebook > become available in your current notebook
# MAGIC * After you attach a notebook to a cluster and run one or more cells, your notebook has state and displays results
# MAGIC * Test
# MAGIC * Databricks has basic version control for notebooks

# COMMAND ----------

dbutils.notebook.run("./1. Pre-requisites", 60)

# COMMAND ----------

# MAGIC %py
# MAGIC myFirstDF.display()

# COMMAND ----------

# MAGIC %python
# MAGIC spark.sql("select * from number_table").display()

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from number_table
