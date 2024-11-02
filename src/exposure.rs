use portable_atomic::AtomicF64;
use pyo3::prelude::*;
use std::sync::atomic::{AtomicI64, Ordering::SeqCst};

#[pyclass(module = "atomicx")]
#[derive(Debug)]
pub struct AtomicInt {
    value: AtomicI64,
}

#[pymethods]
impl AtomicInt {
    #[new]
    #[args(value = "0")]
    fn new(value: i64) -> Self {
        Self {
            value: AtomicI64::new(value),
        }
    }

    pub fn load(&self) -> i64 {
        self.value.load(SeqCst)
    }

    pub fn store(&self, value: i64) {
        self.value.store(value, SeqCst)
    }

    pub fn add(&self, value: i64) -> i64 {
        self.value.fetch_add(value, SeqCst)
    }

    pub fn sub(&self, value: i64) -> i64 {
        self.value.fetch_sub(value, SeqCst)
    }

    pub fn swap(&self, value: i64) -> i64 {
        self.value.swap(value, SeqCst)
    }

    pub fn compare_exchange(&self, current: i64, new: i64) -> (bool, i64) {
        let r = self.value.compare_exchange(current, new, SeqCst, SeqCst);
        (
            r.is_ok(),
            match r {
                Ok(v) => v,
                Err(v) => v,
            },
        )
    }

    pub fn mul(&self, value: i64) -> i64 {
        self.value
            .fetch_update(SeqCst, SeqCst, |v| Some(v * value))
            .unwrap()
    }

    pub fn div(&self, value: i64) -> PyResult<i64> {
        let r = self
            .value
            .fetch_update(SeqCst, SeqCst, |v| v.checked_div(value));
        match r {
            Ok(v) => Ok(v),
            Err(_) => Err(PyErr::new::<pyo3::exceptions::PyZeroDivisionError, _>(
                "division by zero",
            )),
        }
    }

    pub fn __iadd__(&mut self, value: i64) -> PyResult<()> {
        self.value.fetch_add(value, SeqCst);
        Ok(())
    }

    pub fn __isub__(&mut self, value: i64) -> PyResult<()> {
        self.value.fetch_sub(value, SeqCst);
        Ok(())
    }

    pub fn __imul__(&mut self, value: i64) -> PyResult<()> {
        self.value
            .fetch_update(SeqCst, SeqCst, |v| Some(v * value))
            .unwrap();
        Ok(())
    }

    pub fn __idiv__(&mut self, value: i64) -> PyResult<()> {
        let r = self
            .value
            .fetch_update(SeqCst, SeqCst, |v| v.checked_div(value));
        match r {
            Ok(_) => Ok(()),
            Err(_) => Err(PyErr::new::<pyo3::exceptions::PyZeroDivisionError, _>(
                "division by zero",
            )),
        }
    }

    pub fn inc(&self) -> i64 {
        self.value.fetch_add(1, SeqCst)
    }

    pub fn dec(&self) -> i64 {
        self.value.fetch_sub(1, SeqCst)
    }

    pub fn __str__(&self) -> PyResult<String> {
        Ok(self.value.load(SeqCst).to_string())
    }

    pub fn __repr__(&self) -> PyResult<String> {
        Ok(format!(
            "AtomicInt({})",
            self.value.load(std::sync::atomic::Ordering::SeqCst)
        ))
    }

    pub fn __int__(&self) -> PyResult<i64> {
        Ok(self.value.load(SeqCst))
    }

    pub fn __getstate__(&self) -> PyResult<i64> {
        Ok(self.load())
    }

    pub fn __setstate__(&mut self, value: i64) -> PyResult<()> {
        self.store(value);
        Ok(())
    }
}

#[pyclass(module = "atomicx")]
#[derive(Debug)]
pub struct AtomicBool {
    value: std::sync::atomic::AtomicBool,
}

#[pymethods]
impl AtomicBool {
    #[new]
    #[args(value = "false")]
    fn new(value: bool) -> Self {
        Self {
            value: std::sync::atomic::AtomicBool::new(value),
        }
    }

    pub fn load(&self) -> bool {
        self.value.load(SeqCst)
    }

    pub fn store(&self, value: bool) {
        self.value.store(value, SeqCst)
    }

    pub fn swap(&self, value: bool) -> bool {
        self.value.swap(value, SeqCst)
    }

    pub fn compare_exchange(&self, current: bool, new: bool) -> (bool, bool) {
        let r = self.value.compare_exchange(current, new, SeqCst, SeqCst);
        (
            r.is_ok(),
            match r {
                Ok(v) => v,
                Err(v) => v,
            },
        )
    }

    pub fn flip(&self) -> bool {
        self.value.fetch_xor(true, SeqCst)
    }

    pub fn __str__(&self) -> PyResult<String> {
        Ok(self.value.load(SeqCst).to_string())
    }

    pub fn __repr__(&self) -> PyResult<String> {
        Ok(format!(
            "AtomicBool({})",
            self.value.load(std::sync::atomic::Ordering::SeqCst)
        ))
    }

    pub fn __bool__(&self) -> PyResult<bool> {
        Ok(self.value.load(SeqCst))
    }

    pub fn __int__(&self) -> PyResult<i64> {
        Ok(self.value.load(SeqCst) as i64)
    }

    pub fn __invert__(&self) -> PyResult<bool> {
        Ok(!self.value.load(SeqCst))
    }

    pub fn __getstate__(&self) -> PyResult<bool> {
        Ok(self.load())
    }

    pub fn __setstate__(&mut self, value: bool) -> PyResult<()> {
        self.store(value);
        Ok(())
    }
}

#[pyclass(module = "atomicx")]
#[derive(Debug)]
pub struct AtomicFloat {
    value: AtomicF64,
}

#[pymethods]
impl AtomicFloat {
    #[new]
    #[args(value = "0.0")]
    fn new(value: f64) -> Self {
        Self {
            value: AtomicF64::new(value),
        }
    }

    pub fn load(&self) -> f64 {
        self.value.load(SeqCst)
    }

    pub fn store(&self, value: f64) {
        self.value.store(value, SeqCst)
    }

    pub fn add(&self, value: f64) -> f64 {
        self.value.fetch_add(value, SeqCst)
    }

    pub fn sub(&self, value: f64) -> f64 {
        self.value.fetch_sub(value, SeqCst)
    }

    pub fn swap(&self, value: f64) -> f64 {
        self.value.swap(value, SeqCst)
    }

    pub fn compare_exchange(&self, current: f64, new: f64) -> (bool, f64) {
        let r = self.value.compare_exchange(current, new, SeqCst, SeqCst);
        (
            r.is_ok(),
            match r {
                Ok(v) => v,
                Err(v) => v,
            },
        )
    }

    pub fn mul(&self, value: f64) -> f64 {
        self.value
            .fetch_update(SeqCst, SeqCst, |v| Some(v * value))
            .unwrap()
    }

    pub fn div(&self, value: f64) -> PyResult<f64> {
        let r = self.value.fetch_update(SeqCst, SeqCst, |v| match value {
            0.0 => None,
            _ => Some(v / value),
        });
        match r {
            Ok(v) => Ok(v),
            Err(_) => Err(PyErr::new::<pyo3::exceptions::PyZeroDivisionError, _>(
                "division by zero",
            )),
        }
    }

    pub fn __iadd__(&mut self, value: f64) -> PyResult<()> {
        self.value.fetch_add(value, SeqCst);
        Ok(())
    }

    pub fn __isub__(&mut self, value: f64) -> PyResult<()> {
        self.value.fetch_sub(value, SeqCst);
        Ok(())
    }

    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("AtomicFloat({})", self.load()))
    }

    fn __str__(&self) -> PyResult<String> {
        Ok(self.load().to_string())
    }

    fn __float__(&self) -> PyResult<f64> {
        Ok(self.load())
    }

    fn __getstate__(&self) -> PyResult<f64> {
        Ok(self.load())
    }

    fn __setstate__(&mut self, value: f64) -> PyResult<()> {
        self.store(value);
        Ok(())
    }
}
