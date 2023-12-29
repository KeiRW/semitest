API documentation
=================

This section provides detailed API documentation for all public functions
and classes in ``seSemiProfiler``.



Initial Setup
~~~~~


.. module:: scSemiProfiler_dev.initial_setup
.. currentmodule:: scSemiProfiler_dev

.. autosummary::
   :toctree: api

   scSemiProfiler_dev.initial_setup.initsetup



Get Representatives Single-cell (used in example)
~~~~~


.. module:: scSemiProfiler_dev.get_eg_representatives
.. currentmodule:: scSemiProfiler_dev

.. autosummary::
   :toctree: api

   scSemiProfiler_dev.get_eg_representatives.get_eg_representatives


Single-cell Processing & Feature Augmentation
~~~~~


.. module:: scSemiProfiler_dev.singlecell_process
.. currentmodule:: scSemiProfiler_dev

.. autosummary::
   :toctree: api

   scSemiProfiler_dev.singlecell_process.scprocess


Single-cell Inference
~~~~~


.. module:: scSemiProfiler_dev.inference
.. currentmodule:: scSemiProfiler_dev

.. autosummary::
   :toctree: api

   scSemiProfiler_dev.inference.scinfer


Representatives Selection
~~~~~


.. module:: scSemiProfiler_dev.representative_selection
.. currentmodule:: scSemiProfiler_dev

.. autosummary::
   :toctree: api

   scSemiProfiler_dev.representative_selection.activeselection


Utils - Downstream Analysis
~~~~~


.. module:: scSemiProfiler_dev.utils
.. currentmodule:: scSemiProfiler_dev

.. autosummary::
   :toctree: api

   scSemiProfiler_dev.utils.estimate_cost
   scSemiProfiler_dev.utils.visualize_recon
   scSemiProfiler_dev.utils.visualize_inferred
   scSemiProfiler_dev.utils.loss_curve
   scSemiProfiler_dev.utils.assemble_cohort
   scSemiProfiler_dev.utils.assemble_representatives
   scSemiProfiler_dev.utils.compare_umaps
   scSemiProfiler_dev.utils.compare_adata_umaps
   scSemiProfiler_dev.utils.celltype_proportion
   scSemiProfiler_dev.utils.composition_by_group
   scSemiProfiler_dev.utils.geneset_pattern
   scSemiProfiler_dev.utils.celltype_signature_comparison
   scSemiProfiler_dev.utils.rrho
   scSemiProfiler_dev.utils.enrichment_comparison
   scSemiProfiler_dev.utils.get_error
   scSemiProfiler_dev.utils.errorcurve

   

Utils - Statistics
~~~~~


.. module:: scSemiProfiler_dev.utils
.. currentmodule:: scSemiProfiler_dev

.. autosummary::
   :toctree: api

   scSemiProfiler_dev.utils.comb
   scSemiProfiler_dev.utils.hyperp
   scSemiProfiler_dev.utils.hypert
   scSemiProfiler_dev.utils.faiss_knn