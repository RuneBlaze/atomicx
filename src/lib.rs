mod exposure;
use exposure::{AtomicBool, AtomicFloat, AtomicInt};
use pyo3::prelude::*;

#[pymodule]
fn atomicx(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<AtomicInt>()?;
    m.add_class::<AtomicBool>()?;
    m.add_class::<AtomicFloat>()?;
    Ok(())
}
