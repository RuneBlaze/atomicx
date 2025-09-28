mod exposure;
use exposure::{AtomicBool, AtomicFloat, AtomicInt};
use pyo3::prelude::*;

#[pymodule(gil_used = false)]
fn atomicx(_py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<AtomicInt>()?;
    m.add_class::<AtomicBool>()?;
    m.add_class::<AtomicFloat>()?;
    Ok(())
}
