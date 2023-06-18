mod exposure;
use exposure::{AtomicBool, AtomicInt};
use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
fn feo3mics(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<AtomicInt>()?;
    m.add_class::<AtomicBool>()?;
    Ok(())
}
